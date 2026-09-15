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
        # 1. Clean out any leading/trailing spaces the user might have accidentally typed
        clean_phone = value.strip()

        # 2. Check for standard 10-digit formats (starting with 07 or 01)
        if clean_phone.startswith(('07', '01')) and len(clean_phone) == 10:
            return clean_phone

        # 3. Check for international formats (starting with +254 7 or +254 1)
        # Replacing interior double spaces to keep verification smooth
        spaced_phone = clean_phone.replace("  ", " ")
        if spaced_phone.startswith(('+254 7', '+254 1')) and len(spaced_phone) == 14:
            return spaced_phone

        # If it doesn't match either of your rules, reject it instantly!
        raise ValueError("Must match standard format (07xxxxxxxx) or (+254 7xxxxxxxx)")

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int

    class Config:
        from_attributes = True
