from fastapi import FastAPI
from app.api.v1 import customers, products, invoices
from contextlib import asynccontextmanager
from app.infrastructure.db.init_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield
    # Shutdown (si luego necesitas cerrar recursos)


app = FastAPI(
    title="Facturación Electrónica API",
    lifespan=lifespan
    )

app.include_router(customers.router, prefix="/api/v1")
app.include_router(products.router, prefix="/api/v1")
app.include_router(invoices.router, prefix="/api/v1")