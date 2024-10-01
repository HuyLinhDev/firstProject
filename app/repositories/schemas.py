from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date
from ..constants.customer import AccountType, CustomerStatus,  PreferredContactMethod
class CustomerPayload(BaseModel):
    phonenumber: str


class CustomerBase(BaseModel):
    customerid: int
    firstname: str
    lastname: str
    name: str
    accounttype: str
    customerstatus: str
    customersince: date  
    country: str
    notes: Optional[str] = None  
    preferredcontactmethod: Optional[str] = None  
    email: Optional[str] = None  
    state: Optional[str] = None  
    streetaddress: Optional[str] = None  
    postalcode: Optional[str] = None  
    city: Optional[str] = None  
    phonenumber: Optional[str] = None  

    class Config:
        orm_mode = True
        

class CustomerCreation(BaseModel):
    firstname: str
    lastname: str
    name: Optional[str] = None
    accounttype: AccountType
    customerstatus: CustomerStatus
    customersince: Optional[date] = None
    country: Optional[str] = None
    notes: Optional[str] = None
    preferredcontactmethod: PreferredContactMethod
    email: Optional[EmailStr] = None
    state: Optional[str] = None
    streetaddress: Optional[str] = None
    postalcode: Optional[str] = None
    city: Optional[str] = None
    phonenumber: Optional[str] = None

    class Config:
        orm_mode = True

class CustomerResponse(CustomerBase):
    customerid: int

    class Config:
        orm_mode = True
