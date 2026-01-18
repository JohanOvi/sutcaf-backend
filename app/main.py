from fastapi import FastAPI
from app.api.v1 import customers, products, invoices

app = FastAPI(title="Facturación Electrónica API")

app.include_router(customers.router)
app.include_router(products.router)
app.include_router(invoices.router)