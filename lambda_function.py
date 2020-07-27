from utils import *
import json
import traceback
from datetime import date

today = date.today()


def main():
    try:
        configuration = get_configuration()
        bucket = configuration['bucket']

        for path in configuration['paths']:
            s3_key = path.replace('{date}', format(
                today, configuration['dateFormat']))
            file_count = count_s3_objects(
                s3_bucket=bucket, s3_key=s3_key)
                
            if(file_count < int(configuration['threshold'])):
                send_alert_for_path(sns_topic=configuration['snsTopic'], s3_path=''.join(
                    bucket, s3_key), count=file_count)
    except:
        print(traceback.format_exc())


def lambda_handler(event, context):
    main()
    print("S3 function has completed its execution")


if __name__ == "__main__":
    main()
