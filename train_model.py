import pandas as pd
import joblib
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report

data = pd.read_csv("data/training_data.csv")

X = data[["skin_type", "concern", "product_name"]]
y = data["suitable"]

categorical_features = ["skin_type", "concern", "product_name"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=500))
])

model.fit(X, y)

joblib.dump(model, "models/suitability_model.pkl")

print("Model trained successfully!")