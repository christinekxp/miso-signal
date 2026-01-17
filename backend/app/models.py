from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.sql import func

from app.db import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=True)
    price = Column(Float, nullable=True)
    url = Column(String, nullable=False)
    source = Column(String, nullable=False)
    is_small_dog_friendly = Column(Boolean, default=True)
    size_recommendation = Column(String, nullable=True)

    # Timestamps for trend tracking
    first_seen_at = Column(DateTime(timezone=True), server_default=func.now())
    last_seen_at = Column(DateTime(timezone=True), onupdate=func.now())
