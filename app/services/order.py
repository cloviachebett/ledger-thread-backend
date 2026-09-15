from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.order import OrderRepository
from app.repositories.customer import CustomerRepository
from app.schemas.order import OrderCreate
from app.models.order import Order

class OrderService:
    def __init__(self, db: Session):
        self.repository = OrderRepository(db)
        self.customer_repository = CustomerRepository(db)

    def calculate_billing(self, total: float, paid: float):
        balance = total - paid
        if balance <= 0:
            return 0.0, "Fully Paid"
        return balance, "Partially Paid" if paid > 0 else "Unpaid"

    def create_order(self, schema: OrderCreate):
        customer = self.customer_repository.get_by_id(schema.customer_id)
        if not customer:
            raise HTTPException(status_code=404, detail="Assigned customer profiles do not exist")

        balance, status = self.calculate_billing(schema.total_cost, schema.amount_paid)
        db_order = Order(
            customer_id=schema.customer_id,
            clothing_type=schema.clothing_type,
            total_cost=schema.total_cost,
            amount_paid=schema.amount_paid,
            balance_due=balance,
            status=status
        )
        return self.repository.create(db_order)

    def list_orders(self):
        # REMOVED 'await' here
        return self.repository.get_all()

    def apply_payment(self, order_id: int, payment_amount: float):
        order = self.repository.get_by_id(order_id)
        if not order:
            raise HTTPException(status_code=404, detail="Order details not found")
        
        if order.status == "Fully Paid":
            raise HTTPException(status_code=400, detail="This invoice billing ledger is already fully cleared")

        updated_paid = order.amount_paid + payment_amount
        balance, status = self.calculate_billing(order.total_cost, updated_paid)
        
        order.amount_paid = updated_paid
        order.balance_due = balance
        order.status = status
        
        self.repository.db.commit()
        self.repository.db.refresh(order)
        return order
