import json
import joblib
import pandas as pd

model = joblib.load("models/suitability_model.pkl")

with open("data/products.json") as f:
    products = json.load(f)


def recommend_products(skin_type, concern):
    recommended = []
    avoid = []

    for product in products:
        input_df = pd.DataFrame([{
            "skin_type": skin_type,
            "concern": concern,
            "product_name": product["product_name"]
        }])

        prediction = model.predict(input_df)[0]

        if prediction == 1:
            recommended.append(product["product_name"])
        else:
            avoid.append(product["product_name"])

    return recommended, avoid