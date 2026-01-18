from fastapi import APIRouter

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

@router.get("/health")
def health():
    return {"status": "customers ok"}
