from sqlalchemy import Column, Integer, String
from ..database import Base

class Customer(Base):
    __tablename__ = 'customers'

    customerid = Column(Integer, primary_key=True, index=True, autoincrement=True)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    accounttype = Column(String(20), nullable=False) 
    customerstatus = Column(String(50), nullable=False)
    customersince = Column(String(20), nullable=False)
    country = Column(String(20), nullable=False)
    notes = Column(String(100), nullable=True)  
    preferredcontactmethod = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)  
    state = Column(String(20), nullable=False)
    streetaddress = Column(String(100), nullable=False)  
    postalcode = Column(String(20), nullable=False)
    city = Column(String(20), nullable=False)
    phonenumber = Column(String(20), nullable=True)