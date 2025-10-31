# Fault-Tolerant STS Fix

import boto3
import threading
import time
import random
import logging
from botocore.exceptions import ClientError

# Configuration (Replace with your actual ARN)
STS_ROLE_ARN = "arn:aws:iam::123456789012:role/app-role" 

# Global state
_dynamodb_client = None
logger = logging.getLogger('ResilienceApp')

# --- Credential Management Core ---

def _assume_role_and_create_client():
    """Fetches new 12-hour credentials and initializes the global DynamoDB client."""
    sts_client = boto3.client('sts')
    response = sts_client.assume_role(
        RoleArn=STS_ROLE_ARN,
        RoleSessionName='LongLivedSession',
        DurationSeconds=43200  # 12 hours
    )
    
    creds = response['Credentials']
    
    global _dynamodb_client
    _dynamodb_client = boto3.client('dynamodb',
        aws_access_key_id=creds['AccessKeyId'],
        aws_secret_access_key=creds['SecretAccessKey'],
        aws_session_token=creds['SessionToken']
    )
    logger.info("DynamoDB client initialized with fresh 12-hour STS credentials.")
    return _dynamodb_client

def _refresh_credentials_background():
    """
    Background thread to refresh credentials with jitter before they expire.
    This prevents a Thundering Herd on STS.
    """
    # 12 hours (43200s) minus a 5-minute grace period (300s)
    BASE_WAIT_SECONDS = 42900 
    JITTER_RANGE_SECONDS = 3600  # Up to 1 hour of jitter

    while True:
        # Calculate randomized wait time
        jitter = random.randint(0, JITTER_RANGE_SECONDS)
        wait_time = BASE_WAIT_SECONDS + jitter

        logger.info(f"Next STS refresh scheduled in {wait_time // 3600}h {(wait_time % 3600) // 60}m.")
        time.sleep(wait_time)

        try:
            # Attempt to refresh the credentials via control plane call
            _assume_role_and_create_client()
            logger.info("Successfully refreshed long-lived credentials.")
        except ClientError as e:
            # CRITICAL: Control plane is down. Log the error but continue using 
            # the existing (soon-to-expire) credentials.
            logger.error(f"STS refresh failed during outage: {e.response['Error']['Code']}. Continuing with cached client.")
        except Exception as e:
            logger.error(f"Critical error during credential refresh: {e}")

# --- Public API for Application Startup ---

def initialize_long_lived_client():
    """Call this ONCE at application startup."""
    # 1. Initial synchronous load
    _assume_role_and_create_client()
    
    # 2. Start asynchronous background refresh
    thread = threading.Thread(target=_refresh_credentials_background, daemon=True)
    thread.start()
    
    return _dynamodb_client

def get_dynamodb_client():
    """Returns the globally managed client for application use."""
    if _dynamodb_client is None:
        raise RuntimeError("DynamoDB client not initialized. Call initialize_long_lived_client() at startup.")
    return _dynamodb_client

# Call initialize_long_lived_client() from your main application entry point.
