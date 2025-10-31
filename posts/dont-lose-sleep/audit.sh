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

# PUTTING IT ALL TOGETHER
# Find ALL control plane API calls that will kill you.
# Grep for snake_case (Python), PascalCase (JS/Go), & camelCase (Java).
grep -r -i “describeinstances\|assumerole\|getparameter\|describetable\|updatestack\|describestacks\|getsecretvalue\|listtasks\|setdesiredcapacity\|createlogstream\|describekey” .

