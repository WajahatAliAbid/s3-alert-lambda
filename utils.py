import boto3
from datetime import date
import json

def send_alert_for_path(sns_topic: str, s3_path: str, count: int):
    message = f'No files were received on {date.today()} in {s3_path}'
    sns_client = boto3.client('sns')
    response = sns_client.publish(
        TopicArn=sns_topic,
        Subject='S3 Object Alert',
        Message=message,
    )
    print(f'SNS response is {response}')

def count_s3_objects(s3_bucket: str, s3_key: str):
    s3_paginator = boto3.client('s3').get_paginator('list_objects_v2')
    count = 0
    for page in s3_paginator.paginate(Bucket=s3_bucket, Prefix=s3_key):
        if 'Contents' in page:
            count = count + len(page['Contents'])
    return count

def get_configuration():
    with open('config.json') as file:
        return json.load(file)