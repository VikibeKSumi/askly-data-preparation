


if __name__ == "__main__": 
    try:
        import boto3
        from data_cleaning.get_clean_docs import get_clean_docs
        from data_cloud.save_docs_to_cloud import save_docs_to_cloud
        from config.config import config
        from dotenv import load_dotenv
        load_dotenv()


        client = boto3.client("s3")
        BUCKET_NAME = config.BUCKET_NAME
        RAW_PREFIX = config.RAW_PREFIX
        CLEAN_PREFIX = config.CLEAN_PREFIX

        docs = get_clean_docs(
            client=client,
            bucket_name=BUCKET_NAME,
            raw_prefix=RAW_PREFIX
        )
        save_docs_to_cloud(
            client=client,
            bucket_name=BUCKET_NAME,
            prefix=CLEAN_PREFIX,
            docs= docs)
        print("Successfully saved to cloud")
    except Exception as e:
        print(f"An Error Occured: {e}")

