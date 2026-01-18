from app.db import Base, engine, SessionLocal
from app.models import Product
from app.scrapers.example import scrape_example_product

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

data = scrape_example_product()

#Map scraped data into a db entity
product = Product(**data)

# Add and commit
db.add(test_product)
db.commit()
db.add(product)
db.commit()


# Query back to verify
products = db.query(Product).all()
for p in products:
    print(
        f"- ID={p.id} | "
        f"{p.name} | "
        f"${p.price} | "
        f"{p.source} | "
        f"{p.size_recommendation}"
    )

# Close session
db.close()