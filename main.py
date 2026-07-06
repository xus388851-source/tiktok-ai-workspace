from scraper.run import fetch_trending_products
from ranking.viral_score import calculate_viral_score
from scripts.generate_script import generate_script

def main():
    print("🚀 TikTok AI System Starting...")

    products = fetch_trending_products()

    for p in products:
        p["score"] = calculate_viral_score(p)

    products = sorted(products, key=lambda x: x["score"], reverse=True)

    top = products[0]

    print("🔥 TOP PRODUCT:", top["name"])
    print("\n🎬 SCRIPT:\n")
    print(generate_script(top["name"]))

if __name__ == "__main__":
    main()
