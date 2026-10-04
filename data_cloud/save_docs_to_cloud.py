import json
from botocore.client import BaseClient


def save_docs_to_cloud(client: BaseClient, bucket_name: str, prefix: str, docs: list[dict] ):

    for doc in docs:
        json_doc = json.dumps(doc, ensure_ascii=False, indent=2).encode("utf-8")
        client.put_object(
            Bucket=bucket_name,
            Key=f"{prefix}{doc['id']}.json",
            Body=json_doc,
            ContentType="application/json"
        )