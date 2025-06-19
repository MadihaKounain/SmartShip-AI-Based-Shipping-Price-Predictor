# app.py
import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("shipping_model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit Page Config
st.set_page_config(page_title="Shipping Price Predictor", layout="centered")

# Header
st.markdown(
    "<h1 style='text-align: center; color: navy;'>📦 Shipping Price Predictor (INR)</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# Sidebar Input
st.sidebar.header("Enter Shipping Details")

weight = st.sidebar.number_input("Package Weight (kg)", min_value=0.1, max_value=50.0, value=1.0, step=0.1)
distance = st.sidebar.number_input("Shipping Distance (km)", min_value=1, max_value=5000, value=100, step=1)
speed = st.sidebar.radio("Shipping Speed", ["Standard", "Next-day", "Same-day"])

# Map speed to numeric
speed_mapping = {"Standard": 1, "Next-day": 2, "Same-day": 3}
speed_val = speed_mapping[speed]

# Main Section
st.subheader("📋 Summary of Inputs")
st.write(f"**Weight:** {weight} kg")
st.write(f"**Distance:** {distance} km")
st.write(f"**Speed:** {speed}")

# Predict Button
if st.button("🚀 Predict Shipping Price"):
    input_data = np.array([[weight, distance, speed_val]])
    predicted_price_usd = model.predict(input_data)[0]

    # Convert USD to INR (approximate)
    usd_to_inr_rate = 83
    predicted_price_inr = predicted_price_usd * usd_to_inr_rate

    st.markdown("---")
    st.markdown(
        f"<h2 style='color:green;'>Estimated Shipping Price: ₹{predicted_price_inr:,.2f}</h2>",
        unsafe_allow_html=True
    )
