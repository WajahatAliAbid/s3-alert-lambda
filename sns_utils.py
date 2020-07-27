import boto3
from datetime import date

def send_alert_for_path(sns_topic: str, s3_path: str, count: int):
    message = f'No files were received on {date.today()} in {s3_path}'
    sns_client = boto3.client('sns')
    response = sns_client.publish(
        TopicArn=sns_topic,
        Subject='S3 Object Alert',
        Message=message,
    )
    print(f'SNS response is {response}')