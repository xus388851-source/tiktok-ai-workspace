# TikTok Trend Scraper (Mock Version for Structure)

import random

def get_trending_products():
    products = [
        {"name": "Phone Strap Pearl Chain", "views": random.randint(10000, 500000)},
        {"name": "LED Mini Fan Hat", "views": random.randint(10000, 500000)},
        {"name": "Fidget Squishy Toy", "views": random.randint(10000, 500000)},
        {"name": "Cute Phone Charm", "views": random.randint(10000, 500000)}
    ]
    return products

def rank_products(products):
    return sorted(products, key=lambda x: x["views"], reverse=True)

if __name__ == "__main__":
    data = get_trending_products()
    ranked = rank_products(data)

    print("🔥 Top Trending Products:")
    for item in ranked:
        print(item)
