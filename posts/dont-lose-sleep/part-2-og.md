If you’re reading this, your CTO just handed you Part 1 and said “make it happen.” Here’s how.

This document is your complete technical remediation plan. It’s not a strategic discussion; it’s the actual work the team needs to do to survive the next us-east-1 outage. The companies that made it through October 20th already did this work. The 85+ companies that went down hadn’t.

Your goal is simple: Decouple runtime operations from AWS control plane dependencies. When you’re done, your services will keep serving requests even when us-east-1’s control plane is completely offline for 12+ hours.

The Core Principle: Data Plane vs Control Plane

This is the architectural principle that separates companies that survive outages from companies that don’t.

The application’s ability to serve customer requests should depend only on:

Data plane operations (reads/writes to DynamoDB, S3, SQS, RDS, caches)

Locally cached configuration loaded at startup

Credentials issued with 12-hour lifetime and cached locally

The application must never depend on these control plane operations at runtime:

Provisioning new AWS resources (RunInstances, CreateStack)

Dynamically looking up infrastructure state (DescribeInstances, DescribeTable, DescribeStacks)

Refreshing credentials more frequently than once every few hours

Fetching secrets or configuration on every request

Multi-AZ doesn’t save you. Perfect multi-AZ redundancy only protects your data plane from localized service failure. If your application makes control plane calls at runtime, a failure in us-east-1’s global control plane anchor can still take you down, regardless of which region you’re running in. Control plane dependencies are a separate fault domain.

The Audit (Find All Vulnerabilities)

Before you fix anything, you need to know what’s broken. Run these commands in your application codebase to find every control plane dependency:

# Find all control plane API calls that will kill you
grep -r “DescribeInstances\|AssumeRole\|GetParameter\|DescribeTable\|UpdateStack\|DescribeStacks” .
grep -r “describe_instances\|assume_role\|get_parameter\|describe_table\|update_stack\|describe_stacks” .  # Python
grep -r “describeInstances\|assumeRole\|getParameter\|describeTable\|updateStack\|describeStacks” .      # JavaScript

# Find secrets manager calls
grep -r “get_secret_value\|GetSecretValue\|getSecretValue” .

# Find Parameter Store calls
grep -r “get_parameter\|GetParameter\|getParameter” .

# Find ECS service discovery
grep -r “describe_tasks\|DescribeTasks\|describeTasks\|list_tasks\|ListTasks” .

# Find CloudFormation queries
grep -r “describe_stacks\|DescribeStacks\|describeStacks” .

# Find Auto Scaling calls
grep -r “set_desired_capacity\|SetDesiredCapacity\|setDesiredCapacity” .

# Find CloudWatch Logs creation
grep -r “create_log_stream\|CreateLogStream\|createLogStream” .

# Find KMS metadata calls
grep -r “describe_key\|DescribeKey\|describeKey” .


Now go through every match and ask: Is this called during request handling? Is this in a request handler, middleware, connection pool initialization, or anywhere in the hot path? If yes, that’s a vulnerability. Add it to your spreadsheet:

Sort by revenue impact. The top 10 are what you fix first.

Priority Zero: Fix the 60-Minute Death Clock

Everything else in this document is secondary. If you only fix ONE thing, fix this.

The failure of AWS STS (Security Token Service) creates a universal, timed failure across every service using temporary credentials. Most AWS SDKs automatically call AssumeRole to refresh credentials every 45-50 minutes. When STS fails, every service stops working within one hour.

The Problem: SDK Default Credential Refresh

# DANGEROUS: SDK default behavior
client = boto3.client(’dynamodb’)  # Uses default credential chain
# Under the hood, this calls AssumeRole every ~50 minutes at runtime


When us-east-1’s STS control plane failed on October 20th, every service using this pattern died within 45-60 minutes, regardless of which region they were running in.

The Fix: Load Credentials at Startup, Cache for 12 Hours

Step 1: Configure IAM Roles for Maximum Session Duration

Set all application-facing IAM roles to 12 hours (43,200 seconds, the maximum AWS allows):

# AWS CLI
aws iam update-role \
  --role-name your-application-role \
  --max-session-duration 43200

# Terraform
resource “aws_iam_role” “app_role” {
  name               = “application-role”
  max_session_duration = 43200  # 12 hours
  assume_role_policy = jsonencode({...})
}


Step 2: Load Credentials at Application Startup

# FIXED: Load credentials once at startup
import boto3
from botocore.credentials import RefreshableCredentials
from botocore.session import get_session

def get_long_lived_session():
    # Get credentials at startup
    session = boto3.Session()
    credentials = session.get_credentials()
    
    # Create client with explicit credentials
    # These are cached and reused for the lifetime of the process
    client = boto3.client(’dynamodb’,
        aws_access_key_id=credentials.access_key,
        aws_secret_access_key=credentials.secret_key,
        aws_session_token=credentials.token
    )
    return client

# Call this ONCE at app startup, not per request
dynamodb_client = get_long_lived_session()


(Answers to your security team’s inevitable questions follow below.)Step 3: Handle Credential Expiration via Restart

Your applications should restart periodically (every 6-12 hours) as part of normal deployment cycles. When they restart, they get fresh credentials at boot. If credentials expire during runtime:

# Graceful degradation approach
def safe_dynamodb_call():
    try:
        return dynamodb_client.get_item(...)
    except ClientError as e:
        if e.response[’Error’][’Code’] == ‘ExpiredToken’:
            logger.error(”Credentials expired, service restart required”)
            # Option A: Return cached data if available
            # Option B: Fail fast and let orchestration restart the process
            raise
        raise


For JWT/SAML Federation: If you’re using federated identity, set the SAML assertion session lifetime to 12 hours in your IdP (Okta, Azure AD, etc.). This ensures the same long-lived credential behavior.

Yes, your security team will ask about this. Point them to Part 1’s section on the security vs. resilience trade-off and see Q&A, below. You’re not eliminating security, you’re accepting that running instances may operate with expired credentials during a control plane outage, which is preferable to all instances failing simultaneously. 

Test this: Block STS API endpoints at the network level and verify your services continue operating for 12+ hours:

# Block STS control plane
sudo iptables -A OUTPUT -d sts.amazonaws.com -j DROP
sudo iptables -A OUTPUT -d sts.*.amazonaws.com -j DROP

# Verify your services still work
curl http://localhost:8080/health
# Should return 200 OK for the next 12 hours


The Top 9 Control Plane Anti-Patterns (Prioritized)

These are the patterns that killed everyone on October 20th. Fix them in this order.

1. Secrets Manager Reads in Request Hot Path

The Problem:

Every API request fetches secrets from Secrets Manager. While Secrets Manager has a data plane API, it has hidden control plane dependencies on DynamoDB metadata and KMS for decryption.

# DANGEROUS: Every API request fetches secrets
@app.route(’/api/data’)
def get_data():
    secret = secretsmanager.get_secret_value(SecretId=’prod/db/password’)
    db = connect_to_db(password=secret[’SecretString’])
    return db.query()


The Fix:

Load secrets once at application startup and cache them for the app’s lifetime.

# FIXED: Load secrets at startup
import boto3
import os

# Global variable, loaded once at module import
_secrets_cache = {}

def load_secrets_at_startup():
    “”“Call this once when the application starts”“”
    client = boto3.client(’secretsmanager’)
    secret = client.get_secret_value(SecretId=’prod/db/password’)
    _secrets_cache[’db_password’] = secret[’SecretString’]

# Load once at startup
load_secrets_at_startup()

@app.route(’/api/data’)
def get_data():
    # Use cached secret, no API call
    db = connect_to_db(password=_secrets_cache[’db_password’])
    return db.query()


For rotating secrets: Implement a background thread that refreshes every 6+ hours and gracefully handles failures by continuing with the cached value.

import threading
import time

def refresh_secrets_background():
    while True:
        try:
            time.sleep(6 * 60 * 60)  # 6 hours
            client = boto3.client(’secretsmanager’)
            secret = client.get_secret_value(SecretId=’prod/db/password’)
            _secrets_cache[’db_password’] = secret[’SecretString’]
        except Exception as e:
            # Log error but continue with cached secret
            logger.error(f”Secret refresh failed: {e}, using cached value”)

# Start background refresh thread
threading.Thread(target=refresh_secrets_background, daemon=True).start()


2. Parameter Store as Runtime Configuration

The Problem:

Feature flag systems fetch from Parameter Store on every request. Parameter Store has hidden dependencies on KMS metadata and DynamoDB for advanced tier storage.

# DANGEROUS: Fetching feature flags on every request
def is_feature_enabled(feature_name):
    param = ssm.get_parameter(Name=f’/features/{feature_name}’)
    return param[’Parameter’][’Value’] == ‘true’

@app.route(’/api/feature’)
def feature_endpoint():
    if is_feature_enabled(’new_feature’):
        return new_implementation()
    return old_implementation()


The Fix:

Load all parameters at startup with GetParametersByPath, cache locally with 1+ hour TTL, accept stale values during outages.

# FIXED: Load parameters at startup
import boto3
from datetime import datetime, timedelta

_param_cache = {}
_param_cache_time = None
CACHE_TTL = timedelta(hours=1)

def load_parameters_at_startup():
    “”“Call once at startup”“”
    global _param_cache_time
    client = boto3.client(’ssm’)
    
    # Load all parameters with a single API call
    paginator = client.get_paginator(’get_parameters_by_path’)
    for page in paginator.paginate(Path=’/features’, Recursive=True):
        for param in page[’Parameters’]:
            name = param[’Name’].split(’/’)[-1]
            _param_cache[name] = param[’Value’]
    
    _param_cache_time = datetime.now()

# Load once at startup
load_parameters_at_startup()

def is_feature_enabled(feature_name):
    # Use cached value, no API call
    return _param_cache.get(feature_name, ‘false’) == ‘true’

def refresh_parameters_background():
    “”“Background refresh that tolerates failures”“”
    global _param_cache_time
    while True:
        try:
            time.sleep(60 * 60)  # 1 hour
            if datetime.now() - _param_cache_time > CACHE_TTL:
                load_parameters_at_startup()
        except Exception as e:
            # Log error but continue with cached values
            logger.error(f”Parameter refresh failed: {e}, using cached values”)

threading.Thread(target=refresh_parameters_background, daemon=True).start()


Key principle: Prefer availability over perfect freshness. Slightly stale feature flags are better than a completely dead service.

3. Service Discovery via ECS DescribeTasks

The Problem:

Microservices discover backend endpoints by calling ECS DescribeTasks at runtime. This is a pure control plane operation.

# DANGEROUS: Looking up backend service IPs on every request
def get_backend_endpoints():
    tasks = ecs.describe_tasks(
        cluster=’production’,
        tasks=ecs.list_tasks(serviceName=’backend-api’)[’taskArns’]
    )
    return [task[’containers’][0][’networkInterfaces’][0][’privateIpv4Address’]
            for task in tasks[’tasks’]]

@app.route(’/api/proxy’)
def proxy_request():
    endpoints = get_backend_endpoints()  # Control plane call!
    backend = random.choice(endpoints)
    return requests.get(f’http://{backend}/data’)


The Fix:

Use DNS-based service discovery. DNS resolution is pure data plane.

# FIXED: DNS-based service discovery
import socket

@app.route(’/api/proxy’)
def proxy_request():
    # DNS lookup - pure data plane operation
    # ECS Service Discovery creates ‘backend-api.production.local’
    backend_host = ‘backend-api.production.local’
    return requests.get(f’http://{backend_host}/data’)


Setup ECS Service Discovery:

# Terraform: Enable DNS-based service discovery
resource “aws_service_discovery_private_dns_namespace” “internal” {
  name = “production.local”
  vpc  = aws_vpc.main.id
}

resource “aws_service_discovery_service” “backend_api” {
  name = “backend-api”
  dns_config {
    namespace_id = aws_service_discovery_private_dns_namespace.internal.id
    dns_records {
      ttl  = 10
      type = “A”
    }
  }
}

resource “aws_ecs_service” “backend” {
  name    = “backend-api”
  cluster = aws_ecs_cluster.main.id
  
  service_registries {
    registry_arn = aws_service_discovery_service.backend_api.arn
  }
}


Alternative: If you must use ECS APIs, cache discovered endpoints for 5+ minutes and implement graceful degradation with stale lists.

4. Lambda Functions Calling CloudFormation

The Problem:

Lambdas query CloudFormation at runtime to discover resource endpoints.

# DANGEROUS: Lambda querying infrastructure state at runtime
def lambda_handler(event, context):
    cfn = boto3.client(’cloudformation’)
    stack = cfn.describe_stacks(StackName=’my-app-stack’)
    db_endpoint = next(o[’OutputValue’] for o in stack[’Stacks’][0][’Outputs’]
                      if o[’OutputKey’] == ‘DatabaseEndpoint’)
    
    db = connect(db_endpoint)
    return db.query()


The Fix:

Pass configuration via environment variables set at deploy time. CloudFormation evaluates outputs once during deployment.

# FIXED: Use environment variables
import os

def lambda_handler(event, context):
    # Read from environment, no API call
    db_endpoint = os.environ[’DATABASE_ENDPOINT’]
    db = connect(db_endpoint)
    return db.query()


CloudFormation/Terraform setup:

# CloudFormation
Resources:
  MyFunction:
    Type: AWS::Lambda::Function
    Properties:
      Environment:
        Variables:
          DATABASE_ENDPOINT: !GetAtt Database.Endpoint


# Terraform
resource “aws_lambda_function” “api” {
  function_name = “api-handler”
  
  environment {
    variables = {
      DATABASE_ENDPOINT = aws_db_instance.main.endpoint
    }
  }
}


(What? You’re using Pulumi?)

5. DynamoDB Global Tables Metadata Queries

The Problem:

Applications check Global Table replication health via DescribeTable before writes. This requires cross-region control plane coordination.

# DANGEROUS: Checking replication status before writes
def safe_global_write(item):
    table = dynamodb.describe_table(TableName=’GlobalTable’)
    
    # Check if all regions are healthy
    for replica in table[’Table’][’Replicas’]:
        if replica[’ReplicaStatus’] != ‘ACTIVE’:
            raise Exception(”Global table not ready”)
    
    dynamodb.put_item(TableName=’GlobalTable’, Item=item)


The Fix:

Just write to the table. DynamoDB’s data plane handles replication and returns errors if there’s a problem. Trust the data plane.

# FIXED: Write directly, let data plane handle errors
def safe_global_write(item):
    try:
        dynamodb.put_item(TableName=’GlobalTable’, Item=item)
    except ClientError as e:
        # Data plane will tell you if there’s a problem
        if e.response[’Error’][’Code’] == ‘ProvisionedThroughputExceededException’:
            # Handle throttling
            pass
        raise


Key principle: Don’t query metadata to verify health. Let data plane operations fail and handle those failures gracefully.

6. Auto Scaling Based on Application Metrics

The Problem:

Applications directly call Auto Scaling APIs to scale infrastructure.

# DANGEROUS: Application directly calling Auto Scaling APIs
def check_and_scale():
    queue_depth = sqs.get_queue_attributes(
        QueueUrl=’my-queue’,
        AttributeNames=[’ApproximateNumberOfMessages’]
    )
    
    if int(queue_depth[’Attributes’][’ApproximateNumberOfMessages’]) > 1000:
        asg.set_desired_capacity(
            AutoScalingGroupName=’workers’,
            DesiredCapacity=20
        )


The Fix:

Publish custom metrics to CloudWatch (which queues locally), configure CloudWatch alarms with target tracking. AWS handles scaling asynchronously.

# FIXED: Publish metrics, let CloudWatch handle scaling
def publish_queue_depth():
    queue_depth = sqs.get_queue_attributes(
        QueueUrl=’my-queue’,
        AttributeNames=[’ApproximateNumberOfMessages’]
    )
    
    # CloudWatch buffers metrics locally if API unavailable
    cloudwatch.put_metric_data(
        Namespace=’MyApp’,
        MetricData=[{
            ‘MetricName’: ‘QueueDepth’,
            ‘Value’: int(queue_depth[’Attributes’][’ApproximateNumberOfMessages’]),
            ‘Unit’: ‘Count’
        }]
    )

# Background thread publishes metrics every minute
# Your app NEVER calls Auto Scaling APIs directly


CloudWatch Alarm setup:

resource “aws_cloudwatch_metric_alarm” “scale_up” {
  alarm_name          = “queue-depth-high”
  comparison_operator = “GreaterThanThreshold”
  evaluation_periods  = “2”
  metric_name         = “QueueDepth”
  namespace           = “MyApp”
  period              = “60”
  statistic           = “Average”
  threshold           = “1000”
  
  alarm_actions = [aws_autoscaling_policy.scale_up.arn]
}


7. CloudWatch Logs CreateLogStream in Request Path

The Problem:

Applications create log streams synchronously during request handling. CreateLogStream is a control plane operation.

# DANGEROUS: Creating log streams synchronously
def log_request(request_id, data):
    try:
        logs.create_log_stream(
            logGroupName=’/aws/app/requests’,
            logStreamName=request_id
        )
    except logs.exceptions.ResourceAlreadyExistsException:
        pass
    
    logs.put_log_events(
        logGroupName=’/aws/app/requests’,
        logStreamName=request_id,
        logEvents=[{’timestamp’: int(time.time() * 1000), ‘message’: data}]
    )


The Fix:

Write structured logs to stdout/stderr. Configure CloudWatch Agent or Fluent Bit as a sidecar to ship logs asynchronously.

# FIXED: Write to stdout, let agent handle shipping
import json
import sys

def log_request(request_id, data):
    # Write structured JSON to stdout
    log_entry = {
        ‘timestamp’: time.time(),
        ‘request_id’: request_id,
        ‘data’: data
    }
    print(json.dumps(log_entry), file=sys.stdout)


CloudWatch Agent config:

{
  “logs”: {
    “logs_collected”: {
      “files”: {
        “collect_list”: [{
          “file_path”: “/var/log/app/stdout.log”,
          “log_group_name”: “/aws/app/requests”,
          “log_stream_name”: “{instance_id}”
        }]
      }
    }
  }
}


If control plane is down, logs buffer locally. Your application keeps serving requests.

8. KMS DescribeKey in Encryption Hot Path

The Problem:

Checking key metadata before every encryption operation. DescribeKey is control plane, Encrypt is data plane.

# DANGEROUS: Checking key metadata before every encryption
def encrypt_data(plaintext):
    key_metadata = kms.describe_key(KeyId=’alias/my-key’)
    if key_metadata[’KeyMetadata’][’KeyState’] != ‘Enabled’:
        raise Exception(”Key not available”)
    
    return kms.encrypt(KeyId=’alias/my-key’, Plaintext=plaintext)


The Fix:

Call Encrypt directly. The data plane will tell you if the key is unavailable.

# FIXED: Call encrypt directly
def encrypt_data(plaintext):
    try:
        return kms.encrypt(KeyId=’alias/my-key’, Plaintext=plaintext)
    except ClientError as e:
        if e.response[’Error’][’Code’] == ‘DisabledException’:
            logger.error(”KMS key is disabled”)
        raise


Key principle: Don’t preemptively check status. Let data plane operations fail and handle errors gracefully.

9. EC2 DescribeInstances for Health Checks

The Problem:

Applications query EC2 API to verify their own instance health.

# DANGEROUS: Application checking if its own instances are healthy
def health_check():
    my_instance_id = requests.get(’http://169.254.169.254/latest/meta-data/instance-id’).text
    instance = ec2.describe_instances(InstanceIds=[my_instance_id])
    
    state = instance[’Reservations’][0][’Instances’][0][’State’][’Name’]
    return state == ‘running’


The Fix:

Health checks should verify application health, not infrastructure state. If your code is executing, your instance is running.

# FIXED: Check application health, not infrastructure state
def health_check():
    # Verify you can reach your dependencies
    try:
        # Check database connection
        db.execute(’SELECT 1’)
        
        # Check cache
        redis.ping()
        
        # Check you can process a request
        result = process_sample_request()
        
        return {’status’: ‘healthy’}
    except Exception as e:
        return {’status’: ‘unhealthy’, ‘error’: str(e)}


Your load balancer detects unhealthy instances when they stop responding. You don’t need to ask AWS if your instance exists—if your code is running, it exists.

How to Test This: Chaos Engineering

You need to verify your fixes work before the next real outage. Here’s how to simulate a us-east-1 control plane failure.

Network-Level Blocking (Most Realistic)

Block all us-east-1 control plane endpoints at the network level:

# Block us-east-1 control plane
sudo iptables -A OUTPUT -d *.us-east-1.amazonaws.com -j DROP

# Or be more surgical - block specific services
sudo iptables -A OUTPUT -d sts.us-east-1.amazonaws.com -j DROP
sudo iptables -A OUTPUT -d sts.amazonaws.com -j DROP
sudo iptables -A OUTPUT -d dynamodb.us-east-1.amazonaws.com -p tcp --dport 443 -j DROP


AWS Fault Injection Simulator (Managed Chaos)

# Create an experiment that blocks STS
aws fis create-experiment-template \
  --cli-input-json ‘{
    “description”: “Block STS control plane”,
    “actions”: {
      “blockSTS”: {
        “actionId”: “aws:network:disrupt-connectivity”,
        “parameters”: {
          “scope”: “all”,
          “duration”: “PT12H”
        },
        “targets”: {
          “Subnets”: “mySubnets”
        }
      }
    },
    “stopConditions”: [{
      “source”: “none”
    }],
    “roleArn”: “arn:aws:iam::123456789:role/FISRole”,
    “targets”: {
      “mySubnets”: {
        “resourceType”: “aws:ec2:subnet”,
        “selectionMode”: “ALL”
      }
    }
  }’


The Chaos Drill Protocol

Run this quarterly: (or annually if you’re strapped or scrappy.)

Hour 0:00 - Block all *.us-east-1.amazonaws.com at firewall
Hour 0:05 - Verify monitoring detects degraded control plane
Hour 0:15 - Confirm all services still serving requests
Hour 1:00 - Run load tests, verify throughput unchanged
Hour 2:00 - Attempt deployment (should fail gracefully)
Hour 4:00 - Check error logs for control plane call attempts
Hour 8:00 - Verify services still healthy
Hour 12:00 - Restore us-east-1 connectivity
Hour 12:15 - Verify graceful recovery
Hour 24:00 - Post-mortem: what broke?


Target KPIs:

Time to detection: <5 minutes

Customer-facing request success rate: >99.9%

Revenue impact: $0

Data loss: 0 transactions

Services requiring manual intervention: 0

If you don’t hit these KPIs, you found more dependencies. Fix them and test again. Or send an email around if you prefer CYA to hard work. (j/k, please fix.) 

Preemptive Q&A: Handling Pushback

Your team will push back on these changes. Here’s how to win those arguments.

Q: Why is caching configuration for an hour or more acceptable? We need fresh data.

A: We need availability more than we need perfect freshness. Our application will survive an outage by using slightly stale config rather than failing globally because it blocked on a control plane call. If a config change is critical enough to warrant a synchronous API call on every request, it should be baked into a new deployment, not fetched dynamically. Prioritize the data plane.

Q: The Parameter Store API is rated for high throughput. Why is it on the list?

A: High throughput doesn’t equal control plane independence. The API endpoints rely on internal AWS dependencies (KMS metadata for decryption, DynamoDB for advanced tier storage). When those underlying control plane dependencies fail, the high-throughput API fails too. The only way to guarantee resilience is to make the dependency local to your host, which means aggressive caching.

Q: Why can’t we just set a longer timeout and retry?

A: Timeouts and retries are useless against a prolonged control plane outage. You’re just burning compute cycles retrying an API call that’s guaranteed to fail for 6+ hours. The resilient solution is to remove the dependency entirely from the hot path by moving the operation to startup or an asynchronous thread. Retries are for transient data plane faults, not control plane collapse.

Q: Doesn’t the fix for EC2 health checks (removing DescribeInstances) risk missing real infrastructure failures?

A: No. If the instance fails, your process stops, and your load balancer health checks immediately detect the non-responsive port. You’re delegating infrastructure state management to the load balancer and Auto Scaling Group, which is exactly where it belongs. Your application’s job is only to confirm it can execute its business logic. The fix correctly eliminates the circular dependency on EC2 control plane.

Q: Our security team says 12-hour credentials violate our security policy. Isn’t this less secure than 15-minute tokens?

A: It’s true that short TTLs are widely regarded as security best practice. They’re also widely used as a substitute for doing the harder work of building robust security monitoring and defense-in-depth controls. Short TTLs are easy to implement (change a config value) and easy to audit (check a compliance box). But they can become a crutch that delays investment in controls that actually limit blast radius.

Industry standard security frameworks (NIST 800-53, CIS Controls, ISO 27001) prioritize:

Least privilege access controls

Continuous monitoring and anomaly detection

Network segmentation and isolation

Rapid incident response and revocation

Notice what’s not in the top tier? TTL length. That’s an implementation detail, not a foundational control.

Short TTLs reduce the exposure window if credentials are compromised. That’s real. But TTL is an implementation detail, not a foundational security control. Industry standard security frameworks (NIST 800-53, CIS Controls, ISO 27001) prioritize least privilege access controls, continuous monitoring and anomaly detection, network segmentation, and rapid incident response; notice what’s not in the top tier? TTL length. What actually matters when credentials are compromised: Can you detect abnormal usage? What can those credentials access? Can the attacker move laterally? How fast can you revoke them? With robust monitoring and least-privilege policies, you detect and revoke compromised credentials in minutes—whether their TTL is 15 minutes or 12 hours. Without those controls, 15-minute credentials still leave you vulnerable. Companies with 15-minute TTLs and weak monitoring get breached. Companies with 12-hour TTLs and strong monitoring don’t. TTL is a parameter, your security posture is the system. Implement the foundational controls first, then set TTL based on operational requirements.

Q: Our security team still won’t approve 12-hour credentials. What do we do?

A: Point them to Part 1’s ROI calculator. The alternative is accepting that your entire application fails within 15-60 minutes of a control plane outage, costing $X per hour in lost revenue. The security risk of longer-lived credentials is manageable (implement aggressive monitoring, automatic revocation on suspicious activity). The business risk of runtime control plane dependencies is existential. Make them choose between theoretical security risk and actual business risk. (Your CFO may need to referee.)

Success Criteria: You’re Done When...

Here’s your checklist. You’re not done until every item is checked:

✓ Credential Management

[ ] All IAM roles set to 12-hour maximum session duration

[ ] All services load credentials at startup, never refresh at runtime

[ ] Chaos test passes: Services run 12+ hours with STS blocked

✓ Secrets & Configuration

[ ] All secrets loaded at startup, cached for app lifetime

[ ] All Parameter Store reads moved to startup with 1+ hour cache TTL

[ ] Background refresh threads tolerate failures gracefully

✓ Service Discovery

[ ] DNS-based service discovery implemented (no DescribeTasks at runtime)

[ ] All service-to-service calls use DNS names, not IP lookups

✓ Infrastructure Queries

[ ] Zero CloudFormation queries in Lambda runtime (use environment variables)

[ ] Zero DescribeTable calls before DynamoDB operations

[ ] Zero DescribeInstances calls in health checks

✓ Scaling & Monitoring

[ ] Applications publish metrics, never call Auto Scaling APIs directly

[ ] CloudWatch alarms configured for automated scaling

[ ] Logging uses stdout/stderr, no CreateLogStream at runtime

✓ Encryption

[ ] KMS Encrypt calls made directly, no DescribeKey checks

✓ Testing

[ ] Chaos drill completed: Block us-east-1 for 12 hours

[ ] All services continue serving requests

[ ] Monitoring confirms zero control plane calls during drill

[ ] Post-mortem documented any failures found

✓ Documentation

[ ] Runbook updated with control plane failure response

[ ] Team trained on new patterns

[ ] Automated alerts configured for control plane health

Sleep Well

The companies that survived the October 20th outage had already eliminated these dependencies. The companies that didn’t spent 12 hours in war rooms explaining to customers why their beds wouldn’t flatten, why their payments wouldn’t process and why their water purifiers refused to dispense. And explaining to their boss why core services were down despite being “multi-region.”

You have the complete playbook now. Run the audit. Fix priority zero (the 60-minute death clock). Tackle the top 9 anti-patterns. Test it with chaos engineering. Document what you learned. The next us-east-1 outage is coming. Probably within the next 12 months, based on AWS’s track record. The only question is whether you’ll be one of the 85+ companies scrambling in war rooms at 3 AM, or one of the companies who got a good night’s sleep because nobody’s pager duty was going off. 



Never lose another hour of sleep! Subscribe for free to receive new posts and support the work.


