from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.customer import CustomerCreate, CustomerResponse
from app.services.customer import CustomerService
from typing import List

router = APIRouter(prefix="/api/customers", tags=["Customers"])

@router.post("", response_model=CustomerResponse)
def create_customer(schema: CustomerCreate, db: Session = Depends(get_db)):
    service = CustomerService(db)
    
    return service.create_customer(schema)

@router.get("", response_model=List[CustomerResponse])
def get_customers(db: Session = Depends(get_db)):
    service = CustomerService(db)
   
    return service.list_customers()

@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer_by_id(customer_id: int, db: Session = Depends(get_db)):
    service = CustomerService(db)
    
    return service.get_customer_profile(customer_id)
