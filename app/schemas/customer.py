from pydantic import BaseModel, field_validator
from typing import Optional

class CustomerBase(BaseModel):
    name: str
    phone: str
    chest: Optional[float] = 0.0
    waist: Optional[float] = 0.0
    hips: Optional[float] = 0.0
    length: Optional[float] = 0.0
    shoulder: Optional[float] = 0.0

    @field_validator('phone')
    @classmethod
    def check_kenyan_format(cls, value: str) -> str:
        
        clean_phone = value.strip()

        
        if clean_phone.startswith(('07', '01')) and len(clean_phone) == 10:
            return clean_phone

       
        spaced_phone = clean_phone.replace("  ", " ")
        if spaced_phone.startswith(('+254 7', '+254 1')) and len(spaced_phone) == 14:
            return spaced_phone

       
        raise ValueError("Must match standard format (07xxxxxxxx) or (+254 7xxxxxxxx)")

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int

    class Config:
        from_attributes = True
