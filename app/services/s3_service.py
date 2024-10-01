from sqlalchemy import MetaData
from sqlalchemy.orm import Session
import pandas as pd
from io import StringIO
from fastapi.responses import StreamingResponse
from fastapi import UploadFile, HTTPException, status
import boto3
from uuid import uuid4
import os


AWS_BUCKET ='ashavi'
FILE_NAME = 'export (1)'

class S3Service:
    def __init__(self, bucket_name: str):
        self.s3_client = boto3.Session(
            os.getenv("AWS_ACCESS_KEY_ID", ""),
            os.getenv("AWS_SECRECT_ACCESS_KEY", "")
        ).client('s3')
        self.bucket_name = AWS_BUCKET
        
    def upload_csv_to_s3(self, csv: str, content_type: str = 'text/csv'):
        try:
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=FILE_NAME,
                Body=csv,
                ContentType=content_type
            )
            print(f"File {FILE_NAME} uploaded successfully to S3!")
        except Exception as e:
            print(f"Error uploading file: {e}")
            return None

    