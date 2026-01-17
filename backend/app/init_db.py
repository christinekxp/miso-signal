from app.db import Base, engine, SessionLocal
from app.models import Product

# Create all tables in the database
Base.metadata.create_all(bind=engine)
print("✅ Tables created (Base.metadata.create_all called)")

# Open a session
db = SessionLocal()

# Create a product instance
test_product = Product(
    name="Tiny Harness",
    category="clothing",
    price=19.99,
    url="https://example.com/tiny-harness",
    source="Chewy",
    is_small_dog_friendly=True,
    size_recommendation="under 10 lb"
)

# Add and commit
db.add(test_product)
db.commit()

# Query back to verify
product_from_db = db.query(Product).first()
print("Product in DB:", product_from_db.name, product_from_db.price)

# Close session
db.close()