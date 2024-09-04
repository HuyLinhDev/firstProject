from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.repositories.customer_repository import CustomerRepository
from app.services.csv_service import CsvService
from app.repositories.models import Customer
from app.repositories.schemas import CustomerResponse, CustomerPayload, CustomerCreation

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/customers", response_model=list[CustomerResponse])
def get_customers(db: Session = Depends(get_db)):
    repo = CustomerRepository(db)
    customers = repo.get_all_customers()
    return customers

@app.post("/customers", response_model=CustomerResponse)
def get_customer_by_phonenumber(request: CustomerPayload, db: Session = Depends(get_db)):
    repo = CustomerRepository(db)
    customer = repo.get_customer_by_phonenumber(request.phonenumber)
    if customer:
        return customer
    raise HTTPException(status_code=404, detail="Customer not found")

@app.post("/customers/", response_model=CustomerResponse)
def create_customer(customer: CustomerCreation, db: Session = Depends(get_db)):
    repo = CustomerRepository(db)
    db_customer = repo.create_customer(customer)
    if db_customer:
            return db_customer
    raise HTTPException(status_code=400, detail="Failed to create customer")

@app.post("/export/{table_name}")
def download_csv_file(table_name: str, db: Session = Depends(get_db)):
     csv_service = CsvService(db)
     return csv_service.export_table_to_csv(table_name)