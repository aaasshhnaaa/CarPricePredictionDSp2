import streamlit as st
import pandas as pd
import joblib

model = joblib.load("car_price_model.pkl")

st.title("🚗 Car Price Prediction")

st.write("Enter the car details below.")

present_price = st.number_input("Present Price (Lakhs)", min_value=0.0, value=5.0)

kms_driven = st.number_input("Kilometers Driven", min_value=0, value=30000)

fuel_type = st.selectbox(
    "Fuel Type",
    ["CNG", "Diesel", "Petrol"]
)

seller_type = st.selectbox(
    "Seller Type",
    ["Dealer", "Individual"]
)

transmission = st.selectbox(
    "Transmission",
    ["Automatic", "Manual"]
)

owner = st.selectbox(
    "Owner",
    [0, 1, 2, 3]
)

car_age = st.number_input(
    "Car Age (Years)",
    min_value=0,
    value=5
)

fuel_map = {
    "CNG": 0,
    "Diesel": 1,
    "Petrol": 2
}

seller_map = {
    "Dealer": 0,
    "Individual": 1
}

transmission_map = {
    "Automatic": 0,
    "Manual": 1
}

if st.button("Predict Price"):

    features = pd.DataFrame([[
        present_price,
        kms_driven,
        fuel_map[fuel_type],
        seller_map[seller_type],
        transmission_map[transmission],
        owner,
        car_age
    ]], columns=[
        "Present_Price",
        "Kms_Driven",
        "Fuel_Type",
        "Seller_Type",
        "Transmission",
        "Owner",
        "Car_Age"
    ])

    prediction = model.predict(features)

    st.success(f"Estimated Selling Price: ₹ {prediction[0]:.2f} Lakhs")
