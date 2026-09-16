from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

from app.schemas.order import OrderCreate, OrderResponse, PaymentUpdate, OrderUpdateProgress
from app.services.order import OrderService
from typing import List

router = APIRouter(prefix="/api/orders", tags=["Orders"])

@router.post("", response_model=OrderResponse)
def create_order(schema: OrderCreate, db: Session = Depends(get_db)):
    service = OrderService(db)
    return service.create_order(schema)

@router.get("", response_model=List[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    service = OrderService(db)
    return service.list_orders()

@router.patch("/{order_id}/pay", response_model=OrderResponse)
def make_payment(order_id: int, payment: PaymentUpdate, db: Session = Depends(get_db)):
    service = OrderService(db)
    return service.apply_payment(order_id, payment.amount)


@router.patch("/{order_id}", response_model=OrderResponse)
def toggle_order_progress(order_id: int, payload: OrderUpdateProgress, db: Session = Depends(get_db)):
    service = OrderService(db)
    return service.toggle_progress(order_id, payload.is_done)
