from app.db import Base, engine, SessionLocal
from app.models import Product
from app.scrapers.pet_store import scrape_pet_products
from app.util.size_inference import infer_size_info
from app.api.products import get_all_products

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

scraped_products = scrape_pet_products()

# Add and commit
db.add(test_product)

for data in scraped_products:
    existing = (
        db.query(Product)
        .filter(Product.url == data["url"])
        .first()
    )

    size_info = infer_size_info(
        name=data["name"],
        category=data.get("category")
    )
    data.update(size_info)

    if existing:
        existing.price = data["price"]
        existing.last_seen_at = func.now()
        print(f"🔄 Updated: {existing.name}")
    else:
        product = Product(**data)
        db.add(product)
        print(f"✅ Inserted: {data['name']}")

db.commit()


# Query back to verify
products = get_all_products(db)
print("✅ Products in DB:" + str(len(products)))
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