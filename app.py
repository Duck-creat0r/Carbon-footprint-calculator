import streamlit as st
import pandas as pd

st.title("🌍 Carbon Footprint Calculator")

st.write("Please fill in your household information below:")

# Example input fields (you can expand this as needed)
num_people = st.number_input("Number of people in household", min_value=1, max_value=20, value=1)
num_vehicles = st.number_input("Number of vehicles owned", min_value=0, max_value=10, value=0)
km_per_week = st.number_input("Average kilometers driven per week (all vehicles)", min_value=0.0, max_value=10000.0, value=0.0)
uses_public_transport = st.checkbox("Do you use public transport?")
diet_type = st.selectbox("Diet type", ["Regular meat eater", "Occasional meat eater", "Mostly vegetarian", "Vegetarian", "Vegan"])
uses_energy_efficient_appliances = st.checkbox("Use energy-efficient appliances (e.g., LED, inverter ACs)")
use_aircon = st.checkbox("Use air conditioning?")

# Simple emission factors
EMISSION_FACTORS = {
    'vehicle_km': 0.192,  # kg CO2 per km driven
    'public_transport_weekly': 5,  # kg CO2 per week (estimate)
    'diet_regular': 3000,
    'diet_veg': 1500,
    'aircon_per_unit': 1000,  # per year kg CO2 (just example)
}

# Calculate vehicle emissions
vehicle_emission = num_vehicles * km_per_week * EMISSION_FACTORS['vehicle_km'] * 52  # per year

# Calculate public transport emissions
public_transport_emission = EMISSION_FACTORS['public_transport_weekly'] * 52 if uses_public_transport else 0

# Diet emissions based on type
diet_emission_map = {
    "Regular meat eater": EMISSION_FACTORS['diet_regular'],
    "Occasional meat eater": EMISSION_FACTORS['diet_regular'] * 0.75,
    "Mostly vegetarian": EMISSION_FACTORS['diet_regular'] * 0.5,
    "Vegetarian": EMISSION_FACTORS['diet_veg'],
    "Vegan": EMISSION_FACTORS['diet_veg'] * 0.8,
}
diet_emission = diet_emission_map[diet_type]

# Aircon emissions estimate
aircon_emission = EMISSION_FACTORS['aircon_per_unit'] if use_aircon else 0

# Total footprint
total_emission = vehicle_emission + public_transport_emission + diet_emission + aircon_emission

st.subheader("Your Estimated Annual Carbon Footprint (kg CO2):")
st.write(f"**{total_emission:,.0f} kg CO2**")

# Optional: Show breakdown
st.subheader("Breakdown by category:")
st.write(f"Vehicle emissions: {vehicle_emission:,.0f} kg CO2")
st.write(f"Public transport emissions: {public_transport_emission:,.0f} kg CO2")
st.write(f"Diet emissions: {diet_emission:,.0f} kg CO2")
st.write(f"Air conditioning emissions: {aircon_emission:,.0f} kg CO2")
