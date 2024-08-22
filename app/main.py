from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import engine, SessionLocal, Base
from .models import Customer
from .schemas import CustomerResponse, CustomerPayload

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/customers", response_model=list[CustomerResponse])
def get_customers(db: Session = Depends(get_db)):
    customers = db.query(Customer).all()
    return customers

@app.post("/customers", response_model=CustomerResponse)
def get_customer_by_phonenumber(request: CustomerPayload, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter_by(phonenumber=request.phonenumber).first()
    if customer:
        return customer
    raise HTTPException(status_code=404, detail="Customer not found")
