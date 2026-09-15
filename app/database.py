import os  # 1. Import os to read environment variables
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from typing import Generator

# 2. Check for Heroku's database URL first. If not found, use your local fallback.
LOCAL_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/ledger-thread"
DATABASE_URL = os.environ.get("DATABASE_URL", LOCAL_DATABASE_URL)

# 3. Heroku PostgreSQL URLs sometimes start with 'postgres://'. 
# SQLAlchemy requires 'postgresql://'. This line fixes it automatically if needed.
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
