import json

with open("data/ingredients.json") as f:
    ingredients_data = json.load(f)

with open("data/risk_score_mapping.json") as f:
    risk_map = json.load(f)


def analyze_ingredients(user_ingredients):
    total_score = 0
    risky_ingredients = []

    for ing in user_ingredients:
        for item in ingredients_data:
            if ing.lower() == item["ingredient_name"].lower():
                risk_value = risk_map[item["risk_level"]]
                total_score += risk_value

                if item["risk_level"] != "Low":
                    risky_ingredients.append(item["ingredient_name"])

    return total_score, risky_ingredients