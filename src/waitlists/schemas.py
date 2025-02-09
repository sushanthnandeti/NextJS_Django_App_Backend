from ninja import Schema
from datetime import datetime
from pydantic import EmailStr


class WaitListEntryCreateSchema(Schema):
    # Create -> Data
    # Waitlistentryin
    
    email : EmailStr

class WaitListEntryDetailsSchema(Schema):
    # Get -> Data
    # WaitlistentryOut    
    email : EmailStr
    timestamp : datetime