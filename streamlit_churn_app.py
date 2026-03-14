import streamlit as st
import numpy as np

st.set_page_config(page_title="Bank Customer Churn Predictor")

st.title("🏦 Bank Customer Churn Risk Calculator")

st.write("Enter customer details to estimate churn risk.")

# Input features
age = st.slider("Age", 18, 80, 30)

credit_score = st.slider("Credit Score", 300, 900, 600)

balance = st.number_input("Account Balance", min_value=0.0, value=50000.0)

products = st.slider("Number of Products", 1, 4, 2)

active_member = st.selectbox("Is Active Member?", ["Yes", "No"])

# Convert active member
if active_member == "Yes":
    active_member = 1
else:
    active_member = 0

# Predict button
if st.button("Predict Churn Risk"):

    # simple probability logic (demo)
    risk_score = (
        (age/100)*0.3 +
        (1 - credit_score/900)*0.3 +
        (products/4)*0.2 +
        (1-active_member)*0.2
    )

    risk_score = round(risk_score,2)

    st.subheader("Churn Probability")
    st.write(risk_score)

    if risk_score > 0.6:
        st.error("⚠️ High Risk Customer")
    elif risk_score > 0.3:
        st.warning("⚠️ Medium Risk Customer")
    else:
        st.success("✅ Low Risk Customer")

st.write("---")
st.write("Model demonstration for predictive churn analysis project.")
