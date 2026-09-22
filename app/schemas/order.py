from pydantic import BaseModel
from datetime import datetime

class OrderBase(BaseModel):
    customer_id: int
    clothing_type: str
    total_cost: float
    amount_paid: float

class OrderCreate(OrderBase):
    pass



class OrderUpdateProgress(BaseModel):
    is_done: bool


class OrderResponse(OrderBase):
    id: int
    balance_due: float
    status: str
    created_at: datetime
    is_done: bool

    class Config:
        from_attributes = True

class PaymentUpdate(BaseModel):
    amount: float
