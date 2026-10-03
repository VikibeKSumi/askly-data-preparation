from botocore.client import BaseClient

from data_cleaning.clean_markdown import clean_markdown
from data_cleaning.clean_markdown import extract_metadata
from data_cloud.load_doc_from_cloud import load_doc_from_cloud



def prepare_clean_docs(client: BaseClient, bucket_name: str) -> list[dict]:
    docs = []
    resp = client.list_objects_v2(Bucket=bucket_name)
    keys = [obj["Key"] for obj in resp.get("Contents")]

    for key in keys:
        source_uri = f"s3://{bucket_name}/{key}"
        raw = load_doc_from_cloud(client=client, bucket_name=bucket_name, key=key)
        docs.append({
            "id": key,
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
    docs = prepare_clean_doc(client=s3, bucket_name=bucket_name)
    for doc in docs:
        doc["text"] = ""
        print(doc)
        print("-"*80)
