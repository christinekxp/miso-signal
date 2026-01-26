from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_products_returns_list():
    response = client.get("/products")

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)

def test_get_products_schema():
    response = client.get("/products")
    data = response.json()

    if not data:
        return  # no products yet is OK

    product = data[0]

    expected_fields = {
        "id",
        "name",
        "category",
        "price",
        "url",
        "source",
        "is_small_dog_friendly",
        "size_recommendation",
    }

    assert expected_fields.issubset(product.keys())

def test_product_field_types():
    response = client.get("/products")
    data = response.json()

    if not data:
        return

    product = data[0]

    assert isinstance(product["id"], int)
    assert isinstance(product["name"], str)
    assert isinstance(product["price"], (int, float))
    assert isinstance(product["is_small_dog_friendly"], bool)