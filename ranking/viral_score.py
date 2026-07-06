def calculate_viral_score(product):
    """
    简单爆款评分模型
    """

    views = product.get("views", 0)

    # 模拟互动数据（后面可以接TikTok API）
    likes = views * 0.08
    comments = views * 0.01
    shares = views * 0.005

    score = (
        views * 0.5 +
        likes * 0.2 +
        comments * 0.2 +
        shares * 0.1
    )

    return score


if __name__ == "__main__":
    sample = {"name": "Test Product", "views": 100000}
    print("Viral Score:", calculate_viral_score(sample))
