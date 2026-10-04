# askly-data-preparation

An ETL pipline for data that will be used to convert to chunks in the ingestion phase in askly RAG application. It extracts raw markdown from S3, cleans it and extracts metadata into a fixed document schema, and loads it back to S3 as JSON for the RAG ingestion pipeline.

## Features
- AWS S3 bucket storage