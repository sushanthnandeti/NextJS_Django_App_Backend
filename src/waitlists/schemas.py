from ninja import Schema
from datetime import datetime
from pydantic import EmailStr


class WaitListEntryCreateSchema(Schema):
    # Create -> Data
    # Waitlistentryin
    
    email : EmailStr

class WaitListEntryListSchema(Schema):
    # List -> Data
    # WaitlistentryOut    
    id    : int
    email : EmailStr
    

class WaitListEntryDetailSchema(Schema):
    # Get -> Data
    # WaitlistentryOut    
    email : EmailStr
    updated: datetime
    timestamp : datetime