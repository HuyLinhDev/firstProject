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
from fastapi import HTTPException

class CustomerService:
    def __init__(self, db: Session):
        self.repository = CustomerRepository(db)
        self.csv_service = CsvService(db)
        self.s3_service = S3Service(db)
    
    def get_all_customers(self) -> List[Customer]:
        return self.repository.get_all_customers()

    def get_customer_by_phonenumber(self, phonenumber: str) -> Optional[Customer]:
        return self.repository.get_customer_by_phonenumber(phonenumber)

    def create_customer(self, customer_creation: CustomerCreation) -> Optional[Customer]:
        try:
            # Validation: Check if the phone number already exists in the database
            customer = self.repository.get_customer_by_phonenumber(customer_creation.phonenumber)
            if customer:
                print("Error: Phone number already registered")
                raise HTTPException(status_code=400, detail="Phone number already registered")

            db_customer = self.repository.create_customer(customer_creation)
            return db_customer

        except HTTPException as http_exception:
            print(f"HTTPException: {http_exception.detail}")
            raise http_exception  # Re-raise to propagate it up to the FastAPI handler

        except Exception as e:
            print(f"Unexpected error: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")
        
    def create_customer_and_upload_s3(self, customer_creation: CustomerCreation) -> Optional[Customer]:
        try:
            # Validation: Check if the phone number already exists in the database
            customer = self.repository.get_customer_by_phonenumber(customer_creation.phonenumber)
            if customer:
                raise HTTPException(status_code=400, detail="Phone number already registered")

            db_customer = self.repository.create_customer(customer_creation)

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