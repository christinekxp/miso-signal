from typing import Optional, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title="Miso Signal API",
    version="0.1.0",
    description="Starter FastAPI application"
)

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    is_offer: Optional[bool] = False

# simple in-memory store
_items: Dict[int, Item] = {}
_next_id = 1

@app.get("/", tags=["health"])
async def read_root():
    return {"status": "ok"}

@app.post("/items/", response_model=Item, status_code=201, tags=["items"])
async def create_item(item: Item):
    global _next_id
    item.id = _next_id
    _items[_next_id] = item
    _next_id += 1
    return item

@app.get("/items/{item_id}", response_model=Item, tags=["items"])
async def read_item(item_id: int):
    item = _items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)