from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import customer, order

# This instantly creates your PostgreSQL tables synchronously on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ThreadLedger OS")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(customer.router)
app.include_router(order.router)
