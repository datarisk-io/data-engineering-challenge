import os
import boto3
from botocore.client import Config
import logging
from dotenv import load_dotenv

load_dotenv() 
logger = logging.getLogger(__name__)

#MINIO_CONFIGS:

MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "http://localhost:9000")
MINIO_USER = os.getenv("MINIO_ROOT_USER", "rootuser")
MINIO_PASSWORD = os.getenv("MINIO_ROOT_PASSWORD", "rootpassword123")

#Start S3 client looking for MinIO

s3_client = boto3.client(
    "s3",
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=MINIO_USER,
    aws_secret_access_key=MINIO_PASSWORD,
    config=Config(signature_version="s3v4"),
    region_name="us-east-1" # MinIO aceita qualquer região fictícia padrão
)

#Defining Medallion Architecture layers:
layers = ["landing", "raw","trusted","refined"]

def create_data_lake():
    logger.info("Creating data lake structure in MinIO...")
    existing_buckets = [bucket['Name'] for bucket in s3_client.list_buckets().get('Buckets', [])]

    for layer in layers:
        if layer not in existing_buckets:
            s3_client.create_bucket(Bucket=layer)
            logger.info(f"Bucket '{layer}' created successfully.")
        else:
            logger.info(f"Bucket '{layer}' already exists.")

    logger.info("Data lake structure creation completed.")

if __name__ == "__main__":
    create_data_lake()
