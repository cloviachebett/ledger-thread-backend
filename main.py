import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import customer, order

# This instantly creates your PostgreSQL tables synchronously on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ThreadLedger OS")

# allow_origins="*" together with allow_credentials=True is invalid per the
# CORS spec: browsers will reject credentialed requests (cookies/auth
# headers) against a wildcard origin regardless of what the server sends.
# Read allowed origins from an env var so each deployment can set its real
# frontend URL(s); fall back to common local dev ports.
_origins_env = os.environ.get("ALLOWED_ORIGINS")
allow_origins = (
    [o.strip() for o in _origins_env.split(",") if o.strip()]
    if _origins_env
    else ["http://localhost:3000", "http://127.0.0.1:3000"]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(customer.router)
app.include_router(order.router)
