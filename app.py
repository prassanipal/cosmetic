import streamlit as st
from utils.recommender import recommend_products
from utils.risk_analysis import analyze_ingredients

st.set_page_config(page_title="Cosmetic AI Recommender", layout="wide")

# Custom CSS Styling
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .title {
        font-size:40px !important;
        font-weight: bold;
        color: #d63384;
    }
    .subtitle {
        font-size:18px;
        color: gray;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">Hiii beautifull ladies</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Personalized skincare recommendations </p>', unsafe_allow_html=True)

st.markdown("---")

# Layout in 2 columns
col1, col2 = st.columns(2)

with col1:
    skin_type = st.selectbox(
        " Select Your Skin Type",
        ["oily", "dry", "combination", "sensitive"]
    )

with col2:
    concern = st.selectbox(
        " Select Your Skin Concern",
        ["acne", "dullness", "redness", "blackheads"]
    )

ingredients_input = st.text_input("🧪 Enter Ingredients (comma separated)", placeholder="Example: Salicylic Acid, Paraben")

st.markdown("---")

if st.button(" Analyze & Recommend"):

    recommended, avoid = recommend_products(skin_type, concern)

    st.subheader(" Top Recommended Products")

    if recommended:
        for product in recommended:
            st.success(f"✔ {product}")
    else:
        st.info("No strong recommendation found.")

    st.markdown("---")

    st.subheader(" Products You Should Avoid")

    if avoid:
        for product in avoid:
            st.error(f"✘ {product}")

    st.markdown("---")

    # Ingredient Risk Analysis
    if ingredients_input:
        ingredients_list = [x.strip() for x in ingredients_input.split(",")]
        score, risky = analyze_ingredients(ingredients_list)

        st.subheader(" Ingredient Risk Analysis")

        # Risk Meter
        st.progress(min(score / 10, 1.0))

        st.write(f"### 🔢 Total Risk Score: {score}")

        if risky:
            st.warning("⚠ Risky Ingredients Found: " + ", ".join(risky))
        else:
            st.success("✅ All ingredients are considered low risk!")