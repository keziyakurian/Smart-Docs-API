from fastapi import FastAPI
from app.core.config import settings
from app.api import endpoints

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(endpoints.router, prefix=settings.API_V1_STR)

@app.get("/health")
def health_check():
    return {"status": "healthy"}
