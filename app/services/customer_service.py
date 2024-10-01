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
            data = self.repository.get_all_customers()
            csv = self.csv_service.convert_to_csv(data)
            self.s3_service.upload_csv_to_s3_v2(csv)
            return db_customer

        except Exception as e:
            print(f"Error: {e}")
            return e

    def export_customers_to_json(self, file_path: str) -> None:
        customers = self.get_all_customers()
        customers_data = [customer.__dict__ for customer in customers]
        self.repository.convert_to_json_file(customers_data, file_path)