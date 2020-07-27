> AWS Lambda Function to generate alerts using Amazon SNS based on objects in s3 folders
# S3 Alert Lambda
I had a requirement where I needed to configure alarms for objects in s3 bucket. Our clients send files via SFTP which are synced to s3 bucket and arrangd in date vise folder. For example
```
ClientA
- 2020_06_01
- 2020_06_02
- 2020_06_03
- 2020_06_04
ClientB
- 2020_06_03
- 2020_06_04
```
So it was pretty easy to configure lambda function which would count the number of objects and generate alert if there was no data received on a specific day. The lambda function handled configuration in the following format
```json
{
  "bucket": "my-required-s3-bucket",
  "paths": [
    "/ClientA/{date}",
    "/ClientB/{date}",
    "/ClientC/{date}"
  ],
  "dateFormat": "%Y_%m_%d",
  "snsTopic": "my-custom-sns-topic-arn",
  "threshold": 5
}
```
Whenever count of objects is less than the specified threshold, the alert would be sent to a Amazon SNS topic, which I can configure to send email alerts. I had configured this lambda to run at the day end of our clients via Amazon CloudWatch.