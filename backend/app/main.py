from typing import Optional, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.db import SessionLocal
from app.api.products import get_products
from app.api import products
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="Miso Signal API"
)

app.include_router(products.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products")
def get_products():
    db = SessionLocal()
    products = get_products(db)
    db.close()

    return [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "url": p.url,
        }
        for p in products
    ]