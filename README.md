# askly-data-preparation

An ETL pipeline for data that will be used to convert to chunks in the ingestion phase in askly RAG application. It extracts raw markdown from S3, cleans it and extracts metadata into a fixed document schema, and loads it back to S3 as JSON for the RAG ingestion pipeline.

## Part of the Askly system

| Repo | Role |
|---|---|
| **askly-data-preparation** (this repo) | Raw docs → clean JSON (ETL) |
| [askly-ingestion](https://github.com/VikibeKSumi/askly-ingestion) | Clean JSON → chunks → embeddings → Pinecone |
| [askly](https://github.com/VikibeKSumi/askly) | RAG app: query → answer |

**Input:** raw markdown at `s3://askly-bucket/raw/`
**Output:** one JSON per document at `s3://askly-bucket/clean/<id>.json`
(fields: `id`, `title`, metadata, `source_uri`, `text`), consumed by
[askly-ingestion](https://github.com/VikibeKSumi/askly-ingestion).



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
