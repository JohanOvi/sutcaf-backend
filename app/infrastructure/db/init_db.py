from app.infrastructure.db.session import engine
from app.infrastructure.db.base import Base

from app.infrastructure.repositories.customers.customer_model import CustomerModel

def init_db():
    Base.metadata.create_all(bind=engine)