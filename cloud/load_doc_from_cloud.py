import boto3



def load_doc_from_cloud(s3: boto3, bucket_name: str, key: str):
    obj = s3.get_object(Bucket=bucket_name, Key=key)
    raw = obj["Body"].read().decode("utf-8")
    return raw



if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    print(load_doc_from_cloud(s3=boto3.client('s3'), bucket_name="askly-bucket", key="company_operations.md"))