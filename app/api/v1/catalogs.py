from fastapi import APIRouter
from app.infrastructure.external.api_client import ExternalApiClient

router = APIRouter(
    prefix="/catalogs",
    tags=["Catalogs"]
)

client = ExternalApiClient()

@router.get("/municipalities")
def get_municipalities():
    return client.get("/municipalities")
