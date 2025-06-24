import streamlit as st

EMISSION_FACTORS = {
    'vehicle_km': 0.21,               # kg CO2 per km per vehicle
    'public_transport_weekly': 15,   # kg CO2 per week if using public transport
    'aircon_per_unit': 200,           # annual kg CO2 per AC unit
}

EMISSION_FACTORS_MEAT = {
    "Beef": 27,
    "Pork": 12,
    "Chicken": 6,
    "Fish": 8,
    "None": 0,
}

st.title("🌍 Carbon Footprint Calculator")
st.write("Please fill in your household information below:")

num_people = st.number_input("Number of people in household", min_value=1, max_value=20, step=1, value=1)

num_vehicles = st.number_input("Number of vehicles owned", min_value=0, max_value=10, step=1, value=0)
km_per_week = st.number_input("Average kilometers driven per week (all vehicles)", min_value=0, max_value=10000, step=10, value=0)

use_public_transport = st.checkbox("Do you use public transport?")

st.subheader("Diet - Meat Consumption")
meat_type = st.selectbox("Select type of meat you consume", list(EMISSION_FACTORS_MEAT.keys()))
red_meat_servings_per_week = st.number_input("How many servings of this meat do you eat per week?", min_value=0, max_value=14, step=1, value=3)
serving_size_grams = st.number_input("Average serving size (grams)", min_value=50, max_value=500, step=10, value=100)

use_aircon = st.checkbox("Do you use air conditioning?")
num_aircons = 0
if use_aircon:
    num_aircons = st.number_input("Number of air conditioners", min_value=1, max_value=10, step=1, value=1)

vehicle_emission = num_vehicles * km_per_week * EMISSION_FACTORS['vehicle_km'] * 52
public_transport_emission = EMISSION_FACTORS['public_transport_weekly'] * 52 if use_public_transport else 0
diet_emission = (red_meat_servings_per_week * serving_size_grams / 100) * EMISSION_FACTORS_MEAT[meat_type] * 52
aircon_emission = num_aircons * EMISSION_FACTORS['aircon_per_unit'] if use_aircon else 0

total_emission = vehicle_emission + public_transport_emission + diet_emission + aircon_emission

st.subheader("Your Estimated Annual Carbon Footprint (kg CO2):")
st.write(f"{total_emission:,.0f} kg CO2")

st.subheader("Breakdown by category:")
st.write(f"Vehicle emissions: {vehicle_emission:,.0f} kg CO2")
st.write(f"Public transport emissions: {public_transport_emission:,.0f} kg CO2")
st.write(f"Diet emissions: {diet_emission:,.0f} kg CO2")
st.write(f"Air conditioning emissions: {aircon_emission:,.0f} kg CO2")
