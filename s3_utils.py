import boto3

def count_s3_objects(s3bucket: str, s3Key: str):
    s3_paginator = boto3.client('s3').get_paginator('list_objects_v2')
    count = 0
    for page in s3_paginator.paginate(Bucket=s3bucket, Prefix=s3Key):
        if 'Contents' in page:
            count = count + len(page['Contents'])
    return count
    pass
