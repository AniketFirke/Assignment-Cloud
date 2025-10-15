
import json
import boto3
import os
import uuid
s3 = boto3.client('s3')
BUCKET = os.environ.get('BUCKET')

def lambda_handler(event, context):
    
    payload = event.get('body') if isinstance(event, dict) and 'body' in event else event
    if isinstance(payload, str):
        try:
            payload = json.loads(payload)
        except:
            payload = {"raw": payload}
    record_id = str(uuid.uuid4())
    key = f"raw/{record_id}.json"
    s3.put_object(Bucket=BUCKET, Key=key, Body=json.dumps(payload))
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "stored", "key": key})
    }
