from sqlalchemy import Column, Integer, String, Date
from ..database import Base
class Customer(Base):
    __tablename__ = 'customer'

    customerid = Column(Integer, primary_key=True, index=True)
    accounttype = Column(String, nullable=True)
    customersince = Column(Date, nullable=True)
    country = Column(String, nullable=True)
    firstname = Column(String, nullable=False)
    notes = Column(String, nullable=True)
    preferredcontactmethod = Column(String, nullable=True)
    email = Column(String, nullable=True)
    state = Column(String, nullable=True)
    streetaddress = Column(String, nullable=True)
    name = Column(String, nullable=True)
    phonenumber = Column(String, nullable=True)
    lastname = Column(String, nullable=False)
    customerstatus = Column(String, nullable=True)
    postalcode = Column(String, nullable=True)
    city = Column(String, nullable=True)