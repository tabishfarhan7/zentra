from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base 
from app.core.config import settings #type: ignore

# 1) Create the engine (connection to PostgreSQL)
engine = create_engine(
    str(settings.DATABASE_URL),
    echo=True,              # prints SQL queries in terminal (good for dev)
)

# 2) Session local for making DB sessions per request
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 3) Base class for all SQLAlchemy models
Base = declarative_base()

# 4) Dependency: gives a database session to routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
