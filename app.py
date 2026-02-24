import streamlit as st
from utils.recommender import recommend_products
from utils.risk_analysis import analyze_ingredients

st.title("💄 AI Cosmetic Product Suitability Predictor")

skin_type = st.selectbox("Select Skin Type", 
                         ["oily", "dry", "combination", "sensitive"])

concern = st.selectbox("Select Skin Concern",
                       ["acne", "dullness", "redness", "blackheads"])

ingredients_input = st.text_input("Enter Ingredients (comma separated)")

if st.button("Analyze & Recommend"):

    recommended, avoid = recommend_products(skin_type, concern)

    st.subheader("✅ Recommended Products")
    for r in recommended:
        st.success(r)

    st.subheader("❌ Avoid Products")
    for a in avoid:
        st.error(a)

    if ingredients_input:
        ingredients_list = [x.strip() for x in ingredients_input.split(",")]
        score, risky = analyze_ingredients(ingredients_list)

        st.subheader("🧪 Ingredient Risk Analysis")
        st.write("Total Risk Score:", score)

        if risky:
            st.warning("Risky Ingredients Found: " + ", ".join(risky))
        else:
            st.success("All ingredients are low risk!")