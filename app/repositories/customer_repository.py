from sqlalchemy.orm import Session
from typing import List, Optional
from .models import Customer
from .schemas import CustomerCreation
import json
from sqlalchemy.future import select
from sqlalchemy import func

class CustomerRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_customers(self) -> List[Customer]:
        return self.db.query(Customer).all()

    def get_customer_by_phonenumber(self, phonenumber: str) -> Optional[Customer]:
        return self.db.query(Customer).filter_by(phonenumber=phonenumber).first()

    def convert_to_json_file(obj, file_path):
        try:
            with open(file_path, 'w') as file:
                json.dump(obj, file, indent=4)
            print(f"Object successfully written to {file_path}")
        except (TypeError, IOError) as e:
            print(f"An error occurred: {e}")

    def get_max_id(self) -> int:
        max_customer_id = self.db.query(Customer).order_by(Customer.customerid.desc()).first().customerid
        return max_customer_id

    def create_customer(self, customer: CustomerCreation):
        try:
            db_customer = Customer(
                firstname=customer.firstname,
                lastname=customer.lastname,
                name=customer.name,
                accounttype=customer.accounttype,
                customerstatus=customer.customerstatus,
                customersince=customer.customersince,
                country=customer.country,
                notes=customer.notes,
                preferredcontactmethod=customer.preferredcontactmethod,
                email=customer.email,
                state=customer.state,
                streetaddress=customer.streetaddress,
                postalcode=customer.postalcode,
                city=customer.city,
                phonenumber=customer.phonenumber
            )
            self.db.add(db_customer)
            self.db.commit()
            self.db.refresh(db_customer)
            return db_customer
        except Exception as e:
            self.db.rollback()
            print("e: ", e)
