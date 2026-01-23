from sqlalchemy.orm import Session

from app.domain.customers.repository import CustomerRepository
from app.infrastructure.repositories.customers.customer_model import CustomerModel

class SqlAlchemyCustomerRepository(CustomerRepository):

    def create(self, db: Session, customer: CustomerModel):
        db.add(customer)
        db.commit()
        db.refresh(customer)
        return customer

    def get_all(self, db: Session):
        return db.query(CustomerModel).all()

    def get_by_id(self, db: Session, customer_id: int):
        return db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()

    def update(self, db: Session, customer: CustomerModel):
        db.commit()
        db.refresh(customer)
        return customer

    def delete(self, db: Session, customer: CustomerModel):
        db.delete(customer)
        db.commit()
