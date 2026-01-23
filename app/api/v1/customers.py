from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.customers import (
    CustomerCreate,
    CustomerUpdate,
    CustomerResponse
)
from app.infrastructure.db.dependencies import get_db
from app.infrastructure.repositories.customers.sqlalchemy_customer_repository import (SqlAlchemyCustomerRepository)
from app.infrastructure.repositories.customers.customer_model import CustomerModel

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

repo = SqlAlchemyCustomerRepository()

@router.post("/", response_model=CustomerResponse)
def create_customer(payload: CustomerCreate, db: Session = Depends(get_db)):
    customer = CustomerModel(**payload.model_dump())
    return repo.create(db, customer)

@router.get("/", response_model=list[CustomerResponse])
def list_customers(db: Session = Depends(get_db)):
    return repo.get_all(db)

@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = repo.get_by_id(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer(
    customer_id: int,
    payload: CustomerUpdate,
    db: Session = Depends(get_db)
):
    customer = repo.get_by_id(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    for key, value in payload.model_dump().items():
        setattr(customer, key, value)

    return repo.update(db, customer)

@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = repo.get_by_id(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    repo.delete(db, customer)
    return {"message": "Customer deleted"}
