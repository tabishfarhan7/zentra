from fastapi import FastAPI
from scalar_fastapi.scalar_fastapi import get_scalar_api_reference
from app.api.auth_router import router as auth_router #type: ignore
from app.api.prediction_router import router as prediction_router #type: ignore

app = FastAPI()
app.include_router(auth_router)
app.include_router(prediction_router)



@app.get("/scalar",include_in_schema=False)
def get_scalar_api():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="scalar docs"
    )
