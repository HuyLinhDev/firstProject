from fastapi import FastAPI, HTTPException, Depends, UploadFile
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.repositories.customer_repository import CustomerRepository
from app.services.customer_service import CustomerService
from app.services.csv_service import CsvService
from app.services.s3_service import S3Service
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

@app.post("/customers/{CustomerPayload}", response_model=CustomerResponse)
def get_customer_by_phonenumber(request: CustomerPayload, db: Session = Depends(get_db)):
    repo = CustomerRepository(db)
    customer = repo.get_customer_by_phonenumber(request.phonenumber)
    if customer:
        return customer
    raise HTTPException(status_code=404, detail="Customer not found")

@app.post("/customers/", response_model=CustomerResponse)
def create_customer_and_upload_s3(customer: CustomerCreation, db: Session = Depends(get_db)):
    customer_service = CustomerService(db)
    db_customer = customer_service.create_customer_and_upload_s3(customer)
    if db_customer:
        return db_customer
    raise HTTPException(status_code=400, detail="Failed to create customer")

@app.post("/export/{table_name}")
def download_csv_file(table_name: str, db: Session = Depends(get_db)):
    csv_service = CsvService(db)
    return csv_service.export_table_to_csv(table_name)

@app.post("/s3")
async def upload_to_s3(file: UploadFile, db: Session = Depends(get_db)):
    s3_service = S3Service(db)
    result = s3_service.upload_csv_to_s3(file)
    return result