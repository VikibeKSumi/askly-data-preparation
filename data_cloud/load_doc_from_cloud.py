from botocore.client import BaseClient



def load_doc_from_cloud(client : BaseClient, bucket_name: str, key: str):
    obj = client.get_object(Bucket=bucket_name, Key=key)
    raw = obj["Body"].read().decode("utf-8")
    return raw



if __name__ == "__main__":
    import boto3
    from config.config import config
    from dotenv import load_dotenv
    load_dotenv()
    
    s3 = boto3.client("s3")
    BUCKET_NAME = config.BUCKET_NAME
    RAW_PREFIX = config.RAW_PREFIX
    list_object = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=RAW_PREFIX)
    keys = [obj["Key"] for obj in list_object.get("Contents") if not obj["Key"].endswith("/")]
    
    print(load_doc_from_cloud(client=boto3.client('s3'), bucket_name=BUCKET_NAME, key=keys[0]))