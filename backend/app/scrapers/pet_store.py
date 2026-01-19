import requests
from app.util.keywords import DOG_KEYWORDS
from bs4 import BeautifulSoup

BASE_URL = "https://webscraper.io"

def scrape_pet_products():
    url = f"{BASE_URL}/test-sites/e-commerce/static"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    products = []

    for item in soup.select(".thumbnail"):
        name_el = item.select_one(".title")
        price_el = item.select_one(".price")

        if not name_el or not price_el:
            continue

        name = name_el.text.strip()
        name_lower = name.lower()

        # 🐶 POSITIVE dog-only filter
        if not any(keyword in name_lower for keyword in DOG_KEYWORDS):
            continue

        price = float(price_el.text.replace("$", ""))
        product_url = BASE_URL + name_el["href"]

        products.append({
            "name": name,
            "category": "pet_accessory",
            "price": price,
            "url": product_url,
            "source": "WebScraperTestSite",
        })

    return products