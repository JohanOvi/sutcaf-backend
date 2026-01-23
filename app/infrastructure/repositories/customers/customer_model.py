from sqlalchemy import Column, Integer, String
from app.infrastructure.db.session import Base

class CustomerModel(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    identification = Column(String, index=True, nullable=False)
    dv = Column(String, nullable=False)

    company = Column(String, default="")
    trade_name = Column(String, default="")

    names = Column(String, nullable=False)
    address = Column(String, nullable=False)

    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=False)

    legal_organization_id = Column(String, nullable=False)
    tribute_id = Column(String, nullable=False)
    identification_document_id = Column(String, nullable=False)
    municipality_id = Column(String, nullable=False)