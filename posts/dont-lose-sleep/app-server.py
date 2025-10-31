# app-sever.py

import long_lived_client
import logging
from botocore.exceptions import ClientError
from flask import Flask, jsonify, request

# Basic setup
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

# --- Initialization ---
# This is called ONCE when the application starts
try:
    long_lived_client.initialize_long_lived_client()
    DYNAMO_CLIENT = long_lived_client.get_dynamodb_client()
except Exception as e:
    logging.critical(f"Failed to initialize long-lived client at startup: {e}")
    # Application should fail fast if it can't get initial credentials.
    raise

# --- Application Endpoint ---

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user_data(user_id):
    
    try:
        response = DYNAMO_CLIENT.get_item(
            TableName='UserDataTable',
            Key={'UserId': {'N': str(user_id)}}
        )
        return jsonify(response.get('Item', {})), 200

    except ClientError as e:
        error_code = e.response['Error']['Code']
        
        # CRITICAL FAIL-SAFE LOGIC: Handle expired credentials during an outage
        if error_code == 'ExpiredToken':
            logging.error("Credentials expired during request. STS control plane is likely down.")
            # At this point, the application can:
            # 1. Serve stale data from cache (if available)
            # 2. Return Service Unavailable, allowing orchestration to restart/failover (as shown here)
            return jsonify({"error": "Service Unavailable", "reason": "Expired security token."}), 503
        
        # Handle other data plane errors (e.g., throttling)
        return jsonify({"error": "DynamoDB Error", "code": error_code}), 500
    
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
