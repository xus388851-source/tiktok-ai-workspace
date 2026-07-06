from scraper.run import fetch_trending_products
from ranking.viral_score import calculate_viral_score
from scripts.generate_script import generate_script

def main():
    print("🚀 TikTok AI System Starting...")

    # 1. 获取数据
    products = fetch_trending_products()

    # 2. 打分
    for p in products:
        p["score"] = calculate_viral_score(p)

    # 3. 排序
    products = sorted(products, key=lambda x: x["score"], reverse=True)

    top = products[0]

    # 4. 输出结果
    print("\n🔥 TOP PRODUCT:")
    print(top["name"])

    print("\n🎬 SCRIPT:\n")
    print(generate_script(top["name"]))


if __name__ == "__main__":
    main()
