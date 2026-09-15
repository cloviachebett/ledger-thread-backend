from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    chest = Column(Float, default=0.0)
    waist = Column(Float, default=0.0)
    hips = Column(Float, default=0.0)
    length = Column(Float, default=0.0)
    shoulder = Column(Float, default=0.0)

    orders = relationship("Order", back_populates="customer", cascade="all, delete-orphan")
