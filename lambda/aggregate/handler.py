import boto3, json, os, csv, io
from datetime import datetime, timezone
s3 = boto3.client('s3')
BUCKET = os.environ['BUCKET']

def lambda_handler(event, context):
    # Simple example: list objects in raw/ for today and compute count per device
    resp = s3.list_objects_v2(Bucket=BUCKET, Prefix="raw/")
    counts = {}
    for obj in resp.get('Contents', []):
        data = s3.get_object(Bucket=BUCKET, Key=obj['Key'])
        content = json.loads(data['Body'].read())
        device = content.get('device','unknown')
        counts[device] = counts.get(device, 0) + 1

    # Write CSV to reports/
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    csv_buffer = io.StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(["device","count"])
    for k,v in counts.items():
        writer.writerow([k,v])
    key = f"reports/daily-summary-{now}.csv"
    s3.put_object(Bucket=BUCKET, Key=key, Body=csv_buffer.getvalue())
    return {"statusCode":200,"body": json.dumps({"report_key": key})}
