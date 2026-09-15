from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.order import OrderCreate, OrderResponse, PaymentUpdate
from app.services.order import OrderService
from typing import List

router = APIRouter(prefix="/api/orders", tags=["Orders"])

@router.post("", response_model=OrderResponse)
def create_order(schema: OrderCreate, db: Session = Depends(get_db)):
    service = OrderService(db)
    # REMOVED 'await' here
    return service.create_order(schema)

@router.get("", response_model=List[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    service = Session = Depends(get_db)
    service = OrderService(db)
    # REMOVED 'await' here
    return service.list_orders()

@router.patch("/{order_id}/pay", response_model=OrderResponse)
def make_payment(order_id: int, payment: PaymentUpdate, db: Session = Depends(get_db)):
    service = OrderService(db)
    # REMOVED 'await' here
    return service.apply_payment(order_id, payment.amount)
