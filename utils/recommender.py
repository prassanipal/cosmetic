import json
import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "suitability_model.pkl")
model = joblib.load(model_path)

with open(os.path.join(BASE_DIR, "data", "products.json")) as f:
    products = json.load(f)


def recommend_products(skin_type, concern):

    scored_products = []

    for product in products:

        # Rule-based matching score
        rule_score = 0

        if skin_type in product["skin_type"]:
            rule_score += 2

        if concern in product["concern"]:
            rule_score += 3

        # ML prediction probability
        input_df = pd.DataFrame([{
            "skin_type": skin_type,
            "concern": concern,
            "product_name": product["product_name"]
        }])

        probability = model.predict_proba(input_df)[0][1]

        final_score = rule_score + probability

        scored_products.append((product["product_name"], final_score))

    # Sort by score
    scored_products.sort(key=lambda x: x[1], reverse=True)

    # Top 3 recommended
    recommended = [p[0] for p in scored_products[:3]]

    # Bottom 2 avoid
    avoid = [p[0] for p in scored_products[-2:]]

    return recommended, avoid