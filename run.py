from scraper.run import fetch_trending_products
from ranking.viral_score import calculate_viral_score
from scripts.generate_script import generate_script

def run_system():
    print("🚀 STARTING TIKTOK AI AUTOMATION SYSTEM")

    # 1. 获取产品
    products = fetch_trending_products()

    # 2. 打分
    for p in products:
        p["score"] = calculate_viral_score(p)

    # 3. 排序
    ranked = sorted(products, key=lambda x: x["score"], reverse=True)

    top = ranked[0]

    print("\n🔥 TOP VIRAL PRODUCT:")
    print(top["name"])

    print("\n🎬 GENERATED SCRIPT:\n")
    print(generate_script(top["name"]))


if __name__ == "__main__":
    run_system()
