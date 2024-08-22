from pydantic import BaseModel
from typing import Optional
class CustomerPayload(BaseModel):
    phonenumber: str

class CustomerBase(BaseModel):
    customerid: str
    firstname: str
    lastname: str
    accounttype: str
    customerstatus: str
    customersince: str
    country: str
    notes: str
    preferredcontactmethod: str
    email: str
    state: str
    streetaddress: str
    postalcode: str
    city: str
    phonenumber: str

    class Config:
        orm_mode = True

class CustomerResponse(CustomerBase):
    customerid: int

    class Config:
        orm_mode = True
