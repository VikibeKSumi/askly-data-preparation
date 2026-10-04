# askly-data-preparation

An ETL pipeline for data that will be used to convert to chunks in the ingestion phase in askly RAG application. It extracts raw markdown from S3, cleans it and extracts metadata into a fixed document schema, and loads it back to S3 as JSON for the RAG ingestion pipeline.

## Part of the Askly system

| Repo | Role |
|---|---|
| [askly-data-preparation](https://github.com/<you>/askly-data-preparation) | Raw docs → clean JSON (ETL) |
| **askly-ingestion** (this repo) | Clean JSON → chunks → embeddings → Pinecone |
| [askly](https://github.com/<you>/askly) | RAG app: query → answer |

**Input:** clean JSON at `s3://askly-bucket/clean/`, produced by
[askly-data-preparation](https://github.com/<you>/askly-data-preparation).
**Output:** records in Pinecone index `askly-index`, namespace `askly-namespace`
(fields: `text`, `embedding` (1024-d), `sparse_value`, metadata), read by
[askly](https://github.com/<you>/askly).



## Features
- AWS S3 bucket storage

## Configuration
Settings are in [`config/config.yaml`](config/config.yaml):

```yaml
cloud:
  bucket_name: "askly-bucket"   # S3 bucket holding the documents
  raw_prefix: "raw/"            # input: raw markdown files
  clean_prefix: "clean/"        # output: cleaned JSON documents
```

AWS credentials are not stored in this repo. `boto3` picks them up from your environment (`aws configure`, environment variables or an AWS profile).
