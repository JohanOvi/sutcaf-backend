from pydantic import BaseModel, EmailStr

class CustomerBase(BaseModel):
    identification: str
    dv: str
    company: str = ""
    trade_name: str = ""
    names: str
    address: str
    email: EmailStr
    phone: str
    legal_organization_id: str
    tribute_id: str
    identification_document_id: str
    municipality_id: str

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int

    class Config:
        from_attributes = True
