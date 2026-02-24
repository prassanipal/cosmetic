import pandas as pd
import random
import json

# Load products
with open("data/products.json", "r") as f:
    products = json.load(f)

skin_types = ["oily", "dry", "combination", "sensitive"]
concerns = ["acne", "dullness", "redness", "blackheads"]

data = []

for _ in range(150):  # generate 150 rows
    skin = random.choice(skin_types)
    concern = random.choice(concerns)
    product = random.choice(products)

    suitable = 0
    if skin in product["skin_type"] and concern in product["concern"]:
        suitable = random.choices([1, 0], weights=[0.85, 0.15])[0]
    else:
        suitable = random.choices([0, 1], weights=[0.85, 0.15])[0]

    data.append([skin, concern, product["product_name"], suitable])

df = pd.DataFrame(data, columns=["skin_type", "concern", "product_name", "suitable"])
df.to_csv("data/training_data.csv", index=False)

print("Dataset generated successfully!")