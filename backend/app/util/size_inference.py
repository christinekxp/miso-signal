def infer_size_info(name: str, category: str | None):
    name_lower = name.lower()

    small_keywords = [
        "tiny",
        "toy",
        "xs",
        "small",
        "mini",
        "teacup"
    ]

    for keyword in small_keywords:
        if keyword in name_lower:
            return {
                "is_small_dog_friendly": True,
                "size_recommendation": "under 10 lb"
            }

    return {
        "is_small_dog_friendly": False,
        "size_recommendation": None
    }
