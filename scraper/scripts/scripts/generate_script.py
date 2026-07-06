def generate_ugc_script(product_name):
    return f"""
Hook (0-3s):
Wait... why is everyone buying this {product_name}?!

Problem:
Most people struggle with boring / low-quality versions.

Solution:
This upgraded version is trending on TikTok right now.

CTA:
You can get it before it sells out.
"""

if __name__ == "__main__":
    print(generate_ugc_script("Phone Strap Pearl Chain"))
