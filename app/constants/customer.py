from enum import Enum

class AccountType(str, Enum):
    PREMIUM = "Premium"
    REGULAR = "Regular"

class CustomerStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"