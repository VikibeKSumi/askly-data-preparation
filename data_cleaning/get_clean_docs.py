from botocore.client import BaseClient
from pathlib import Path

from data_cleaning.clean_markdown import clean_markdown
from data_cleaning.extract_metadata import extract_metadata
from data_cloud.load_doc_from_cloud import load_doc_from_cloud



def get_clean_docs(client: BaseClient, bucket_name: str, raw_prefix: str) -> list[dict]:
    docs = []
    resp = client.list_objects_v2(Bucket=bucket_name, Prefix=raw_prefix)
    keys = [obj["Key"] for obj in resp.get("Contents", []) if not obj["Key"].endswith("/")]


    for key in keys:
        source_uri = f"s3://{bucket_name}/{key}"
        raw = load_doc_from_cloud(client=client, bucket_name=bucket_name, key=key)
        docs.append({
            "id": Path(key).stem,
            **extract_metadata(raw),
            "source_uri": source_uri,
            "text": clean_markdown(raw),
        })

    return docs

if __name__ == "__main__":

    import boto3
    from dotenv import load_dotenv
    load_dotenv()

    s3 = boto3.client("s3")
    bucket_name = "askly-bucket"
    docs = get_clean_docs(client=s3, bucket_name=bucket_name, raw_prefix="raw/")
    for doc in docs:
        doc["text"] = ""
        print(doc)
        print("-"*80)
