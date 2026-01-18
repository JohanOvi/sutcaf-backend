from fastapi import APIRouter

router = APIRouter(
    prefix="/invoices",
    tags=["Invoices"]
)

@router.get("/health")
def health():
    return {"status": "invoices ok"}