from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.customer import CustomerRepository
from app.schemas.customer import CustomerCreate

class CustomerService:
    def __init__(self, db: Session):
        self.repository = CustomerRepository(db)

    def create_customer(self, schema: CustomerCreate):
        existing = self.repository.get_by_phone(schema.phone)
        if existing:
            raise HTTPException(status_code=400, detail="Customer with this phone number already exists")
        return self.repository.create(schema)

    def list_customers(self):
       
        return self.repository.get_all()

    def get_customer_profile(self, customer_id: int):
       
        customer = self.repository.get_by_id(customer_id)
        if not customer:
            raise HTTPException(status_code=404, detail="Customer records not found")
        return customer
