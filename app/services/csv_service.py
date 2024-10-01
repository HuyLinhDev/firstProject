from sqlalchemy import MetaData
from sqlalchemy.orm import Session
from typing import List
import pandas as pd
from io import StringIO
from fastapi.responses import StreamingResponse
from io import StringIO
import csv
from ..repositories.models import Customer
class CsvService:
    def __init__(self, db: Session):
        self.db = db

    async def export_table_to_csv(self, table_name: str):
        try:
            metadata = MetaData()
            metadata.reflect(bind=self.db.bind)  
            data = pd.read_sql_table(table_name, con=self.db.bind)
            csv = self.convert_to_csv(data)

            return csv
        except Exception as e:
            raise RuntimeError(f"Failed to export table to CSV: {str(e)}")
        
    def convert_to_csv(self, data: List[Customer]):
        try:
            output = StringIO()
            writer = csv.writer(output)

            headers = [
                'customerid', 
                'firstname', 
                'lastname',
                'name',
                'accounttype',
                'customerstatus',
                'customersince',
                'country',
                'notes',
                'preferredcontactmethod',
                'email',
                'state',
                'streetaddress',
                'postalcode',
                'city',
                'phonenumber',
            ]
            writer.writerow(headers)

            for customer in data:
                writer.writerow(
                    [
                        customer.customerid, 
                        customer.firstname, 
                        customer.lastname,
                        customer.name,
                        customer.accounttype,
                        customer.customerstatus,
                        customer.customersince,
                        customer.country,
                        customer.notes,
                        customer.preferredcontactmethod,
                        customer.email,
                        customer.state,
                        customer.streetaddress,
                        customer.postalcode,
                        customer.city,
                        customer.phonenumber,
                    ]
                )  
            return output.getvalue()
        except Exception as e:
            raise RuntimeError(f"Failed to export table to CSV: {str(e)}")

