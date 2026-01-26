from pydantic import BaseModel
from typing import Optional


class ProductResponse(BaseModel):
    id: int
    name: str
    category: str
    price: float
    url: str
    source: str

    is_small_dog_friendly: bool
    size_recommendation: Optional[str]


    #Object comes from ORM (object relational mapping) model
    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    name: str
    category: str
    price: float
    url: str
    source: str

    is_small_dog_friendly: bool
    size_recommendation: Optional[str]