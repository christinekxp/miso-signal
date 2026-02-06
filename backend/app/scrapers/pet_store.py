import requests
from bs4 import BeautifulSoup
from rapidfuzz import fuzz
import re

from app.util.keywords import DOG_KEYWORDS
from app.db import get_existing_products, save_product  # hypothetical DB helpers

BASE_URL = "https://webscraper.io"

def scrape_pet_products():
    url = f"{BASE_URL}/test-sites/e-commerce/static"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    if response.status_code != 200:
        print("Failed to fetch page")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    existing_products = get_existing_products()  # returns list of dicts with 'name' keys


    products = []

    for item in soup.select(".thumbnail"):
        name_el = item.select_one(".title")
        price_el = item.select_one(".price")
        desc_el = item.select_one(".description")  # optional description


        if not name_el or not price_el:
            continue

        name = name_el.text.strip()
        name_lower = name.lower()
        description = desc_el.text.strip() if desc_el else ""


        # 🐶 POSITIVE dog-only filter
        if not any(keyword in name_lower for keyword in DOG_KEYWORDS.get("all", [])):
            continue

        # Small dog classification
        small_dog = classify_small_dog(name, description)

        # Weight inference
        max_weight = extract_max_weight(description)

        price = float(price_el.text.replace("$", ""))
        product_url = BASE_URL + name_el["href"]

        products.append({
            "name": name,
            "category": "pet_accessory",
            "price": price,
            "url": product_url,
            "small_dog": small_dog,
            "max_weight": max_weight,
            "source": "WebScraperTestSite",
        })

        # Deduplication
        if is_duplicate(product_data, existing_products):
            print(f"Skipping duplicate: {name}")
            continue

        # Save to DB
        save_product(product_data)

        products.append(product_data)

    return products


def classify_small_dog(title, description):
    combined = f"{title.lower()} {description.lower()}"
    return any(keyword in combined for keyword in DOG_KEYWORDS.get("small", []))

def extract_max_weight(description):
    match = re.search(r'up to (\d+)\s?(lbs|kg)', description.lower())
    if match:
        weight, unit = match.groups()
        weight = int(weight)
        if unit == "kg":
            weight *= 2.20462
        return weight
    return None

def is_duplicate(new_product, existing_products, threshold=90):
    for prod in existing_products:
        if fuzz.ratio(new_product['name'], prod['name']) > threshold:
            return True
    return False