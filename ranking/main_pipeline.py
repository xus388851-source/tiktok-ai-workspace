from scraper.run import fetch_trending_products
from ranking.viral_score import calculate_viral_score
from scripts.generate_script import generate_script

def run_pipeline():
    products = fetch_trending_products()

    scored = []
    for p in products:
        p["score"] = calculate_viral_score(p)
        scored.append(p)

    ranked = sorted(scored, key=lambda x: x["score"], reverse=True)

    top = ranked[0]

    print("🔥 TOP PRODUCT:", top["name"])
    print(generate_script(top["name"]))


if __name__ == "__main__":
    run_pipeline()
