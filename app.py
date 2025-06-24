import streamlit as st

st.title("🌍 Carbon Footprint Calculator")

# Household inputs
num_people = st.number_input("Number of people in household", min_value=1, max_value=20, step=1, value=1)
num_vehicles = st.number_input("Number of vehicles owned", min_value=0, max_value=10, step=1, value=0)
km_per_week = st.number_input("Average kilometers driven per week (all vehicles)", min_value=0, max_value=10000, step=10, value=0)
use_public_transport = st.checkbox("Do you use public transport?", value=False)

# Diet inputs (meat consumption)
meat_type = st.selectbox("Select type of meat you consume", list(EMISSION_FACTORS_MEAT.keys()))
red_meat_servings_per_week = st.slider("How many servings of this meat do you eat per week?", 0, 14, 3)
serving_size_grams = st.number_input("Average serving size (grams)", min_value=50, max_value=500, value=100)

# Aircon inputs
use_aircon = st.checkbox("Do you use air conditioning?", value=False)
num_aircons = 0
if use_aircon:
    num_aircons = st.number_input("Number of air conditioners", min_value=1, max_value=10, step=1, value=1)

# Then calculations and output...
