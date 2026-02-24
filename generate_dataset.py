import pandas as pd
import random
import json

# Load products
with open("data/products.json", "r") as f:
    products = json.load(f)

skin_types = ["oily", "dry", "combination", "sensitive"]
concerns = ["acne", "dullness", "redness", "blackheads"]

data = []

for _ in range(3000):   # 🔥 3000 rows
    skin = random.choice(skin_types)
    concern = random.choice(concerns)
    product = random.choice(products)

    # Strong rule logic
    if skin in product["skin_type"] and concern in product["concern"]:
        suitable = random.choices([1, 0], weights=[0.9, 0.1])[0]
    elif skin in product["skin_type"]:
        suitable = random.choices([1, 0], weights=[0.7, 0.3])[0]
    elif concern in product["concern"]:
        suitable = random.choices([1, 0], weights=[0.6, 0.4])[0]
    else:
        suitable = random.choices([0, 1], weights=[0.9, 0.1])[0]

    data.append([skin, concern, product["product_name"], suitable])

df = pd.DataFrame(data, columns=["skin_type", "concern", "product_name", "suitable"])

# 🔥 Balance dataset
ones = df[df["suitable"] == 1]
zeros = df[df["suitable"] == 0]

min_len = min(len(ones), len(zeros))
df_balanced = pd.concat([
    ones.sample(min_len),
    zeros.sample(min_len)
]).sample(frac=1).reset_index(drop=True)

df_balanced.to_csv("data/training_data.csv", index=False)

print("🔥 Large balanced dataset generated successfully!")