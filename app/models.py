from sqlalchemy import Column, Integer, String
from .database import Base

class Customer(Base):
    __tablename__ = 'customers'

    customerid = Column(String(100), primary_key=True, index=True)  # Changed to customerid
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    accounttype = Column(String(20), nullable=False)  # Adjusted to match varchar(20)
    customerstatus = Column(String(50), nullable=False)
    customersince = Column(String(20), nullable=False)
    country = Column(String(20), nullable=False)
    notes = Column(String(100), nullable=True)  # Adjusted to match varchar(100)
    preferredcontactmethod = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)  # Adjusted to match varchar(100)
    state = Column(String(20), nullable=False)
    streetaddress = Column(String(100), nullable=False)  # Adjusted to match varchar(100)
    postalcode = Column(String(20), nullable=False)
    city = Column(String(20), nullable=False)
    phonenumber = Column(String(20), nullable=True)