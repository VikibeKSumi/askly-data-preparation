from botocore.client import BaseClient



def load_doc_from_cloud(client : BaseClient, bucket_name: str, key: str):
    obj = client.get_object(Bucket=bucket_name, Key=key)
    raw = obj["Body"].read().decode("utf-8")
    return raw



if __name__ == "__main__":
    import boto3
    from dotenv import load_dotenv
    load_dotenv()
    
    print(load_doc_from_cloud(client=boto3.client('s3'), bucket_name="askly-bucket", key="company_operations.md"))