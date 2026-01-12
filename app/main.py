from fastapi import FastAPI
from scalar_fastapi.scalar_fastapi import get_scalar_api_reference
from contextlib import asynccontextmanager

from app.api.auth_router import router as auth_router #type: ignore
from app.api.prediction_router import router as prediction_router #type: ignore
from app.api.profile_router import router as profile_router #type: ignore
from app.db.database import Base, engine #type: ignore

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Create database tables on startup"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Cleanup on shutdown
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(prediction_router)


@app.get("/scalar",include_in_schema=False)
def get_scalar_api():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="scalar docs"
    )

