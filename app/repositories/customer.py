from sqlalchemy.orm import Session
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate
from typing import List

class CustomerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, schema: CustomerCreate) -> Customer:
        db_customer = Customer(**schema.model_dump())
        self.db.add(db_customer)
        self.db.commit()
        self.db.refresh(db_customer)
        return db_customer

    def get_all(self) -> List[Customer]:
        return self.db.query(Customer).order_by(Customer.name).all()

    def get_by_id(self, customer_id: int) -> Customer | None:
        """Finds a customer by their unique database primary key ID."""
        return self.db.query(Customer).filter(Customer.id == customer_id).first()

    def get_by_phone(self, phone: str) -> Customer | None:
        """Finds a customer by their phone number to prevent duplicate profile entries."""
        return self.db.query(Customer).filter(Customer.phone == phone).first()
