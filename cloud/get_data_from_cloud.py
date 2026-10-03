

import boto3


def get_data_from_cloud(s3: boto3, bucket_name: str, key: str):
    obj = s3.get_object(Bucket=bucket_name, Key=key)
    raw = obj["Body"].read().decode("utf-8")
    return raw
