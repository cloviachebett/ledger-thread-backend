from sqlalchemy.orm import Session
from app.models.order import Order
from typing import List

class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, order: Order) -> Order:
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order

    def get_all(self) -> List[Order]:
       
        return self.db.query(Order).order_by(Order.created_at.asc()).all()

    def get_by_id(self, order_id: int) -> Order | None:
        return self.db.query(Order).filter(Order.id == order_id).first()
