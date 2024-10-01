from sqlalchemy import MetaData
from sqlalchemy.orm import Session
from typing import List, Optional
import pandas as pd
from ..repositories.models import Customer
from ..repositories.schemas import CustomerCreation
from io import StringIO
from fastapi.responses import StreamingResponse
from ..repositories.customer_repository import CustomerRepository
from .csv_service import CsvService
from .s3_service import S3Service

class CustomerService:
    def __init__(self, db: Session):
        self.repository = CustomerRepository(db)
        self.csv_service = CsvService(db)
        self.s3_service = S3Service(db)
    
    def get_all_customers(self) -> List[Customer]:
        return self.repository.get_all_customers()

    def get_customer_by_phonenumber(self, phonenumber: str) -> Optional[Customer]:
        return self.repository.get_customer_by_phonenumber(phonenumber)

    def create_customer(self, customer: CustomerCreation) -> Optional[Customer]:
        try:
            db_customer = self.repository.create_customer(customer)
            return db_customer

        except Exception as e:
            print(f"Error: {e}")
            return e
        
    def create_customer_and_upload_s3(self, customer: CustomerCreation) -> Optional[Customer]:
        try:
            db_customer = self.repository.create_customer(customer)

            if not db_customer:
                print("Failed to create customer")
                return None

            data = self.repository.get_all_customers()
            if not data:
                print("Failed to retrieve customer data")
                return db_customer

            csv = self.csv_service.convert_to_csv(data)
            if not csv:
                print("Failed to convert customer data to CSV")
                return db_customer

            self.s3_service.upload_csv_to_s3(csv)
            return db_customer
        except Exception as e:
            print(f"Error: {e}")
            return e