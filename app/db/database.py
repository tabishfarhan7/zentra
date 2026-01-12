from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from app.core.config import settings #type: ignore

# DATABASE_URL should be postgresql+psycopg:// in .env for async support
DATABASE_URL = str(settings.DATABASE_URL)

# 1) Create async engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True
)

# 2) Async session maker
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)

# 3) Base class for all SQLAlchemy models
Base = declarative_base()

# 4) Async dependency: gives a database session to routes
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

