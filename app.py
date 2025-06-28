import streamlit as st

# Emission factors (kg CO2e per unit)
EMISSION_FACTORS = {
    'vehicle_km': 0.21,  # per km driven
    'public_transport_weekly': 2.0,  # per week if used
    'diet_vegan': 1500,
    'diet_mostly_vegetarian': 2000,
    'diet_occasional_meat': 2500,
    'diet_regular_meat_eater': 3000,
    'aircon_per_unit': 500,
    'energy_efficiency_factor': 0.8,
    'clothes_per_month': 100,
    'compost_reduction': 200,
    'water_saving_factor': 0.7,
    'shower_minute': 2,
    'electricity_per_kwh': 0.56,  # average Malaysia grid kg CO2/kWh
}

st.title("🌍 Carbon Footprint Calculator")

st.write("Please fill in your household information below:")

# Inputs
st.subheader("Household Composition")

num_adults = st.number_input("Number of adults (18+ years)", min_value=0, max_value=20, value=2)
num_teens = st.number_input("Number of teenagers (13-17 years)", min_value=0, max_value=20, value=1)
num_children = st.number_input("Number of children (0-12 years)", min_value=0, max_value=20, value=0)

total_people_weighted = (num_adults * 1.0) + (num_teens * 0.8) + (num_children * 0.5)

energy_type = st.selectbox(
    "Primary energy type for household electricity",
    ["Grid electricity", "Solar", "Other renewable", "Fossil fuels"]
)

# New electricity usage input
st.subheader("Electricity Usage")
monthly_kwh = st.number_input("Average monthly electricity usage (in kWh)", min_value=0, max_value=10000, value=400)

use_aircon = st.checkbox("Do you use air-conditioning at home?")
num_aircons = 0
if use_aircon:
    num_aircons = st.number_input("Number of air-conditioners in your home", min_value=1, max_value=10, value=1)

use_energy_efficient_appliances = st.checkbox("Do you use energy-efficient appliances? (e.g., inverter ACs, LED lights, energy-rated fridge)")

vehicle_ownership = st.checkbox("Do you or your parents own a vehicle?")
num_vehicles = 0
km_per_week = 0.0
if vehicle_ownership:
    num_vehicles = st.number_input("Number of vehicles owned", min_value=1, max_value=10, value=1)
    km_per_week = st.number_input("Average kilometers driven per week (all vehicles)", min_value=0.0, max_value=10000.0, value=100.0)

use_public_transport = st.checkbox("Do you use public transport?")

diet_type = st.selectbox(
    "Diet type",
    ["Vegan", "Mostly vegetarian", "Occasional meat eater", "Regular meat eater"]
)

use_water_saving_fixtures = st.checkbox("Do you use water-saving fixtures (low-flow taps/showers)?")

showers_per_day = st.number_input("How many showers are taken daily in your household (on average)?", min_value=0, max_value=50, value=2)

shower_duration_min = st.number_input("Average duration of a shower (in minutes)?", min_value=0, max_value=60, value=5)

compost_food_waste = st.checkbox("Do you compost food waste?")

clothes_buy_freq = st.selectbox(
    "How often do you buy new clothes or fashion items?",
    ["Never", "Rarely", "Monthly", "Weekly"]
)


# Calculations

# Diet emission by type
diet_emission_map = {
    "Vegan": EMISSION_FACTORS['diet_vegan'],
    "Mostly vegetarian": EMISSION_FACTORS['diet_mostly_vegetarian'],
    "Occasional meat eater": EMISSION_FACTORS['diet_occasional_meat'],
    "Regular meat eater": EMISSION_FACTORS['diet_regular_meat_eater'],
}

diet_emission = diet_emission_map[diet_type]

# Vehicle emissions
vehicle_emission = num_vehicles * km_per_week * EMISSION_FACTORS['vehicle_km'] * 52 if vehicle_ownership else 0

# Public transport emission
public_transport_emission = EMISSION_FACTORS['public_transport_weekly'] * 52 if use_public_transport else 0

# Aircon emissions
aircon_emission = num_aircons * EMISSION_FACTORS['aircon_per_unit'] if use_aircon else 0

# Energy efficiency adjustment (appliances)
energy_efficiency_adj = 1.0
if use_energy_efficient_appliances:
    energy_efficiency_adj = EMISSION_FACTORS['energy_efficiency_factor']

# Clothes emissions
clothes_freq_map = {
    "Never": 0,
    "Rarely": 50,
    "Monthly": EMISSION_FACTORS['clothes_per_month'],
    "Weekly": 200,
}

clothes_emission = clothes_freq_map[clothes_buy_freq] * 12  # annual

# Compost reduction
compost_reduction = EMISSION_FACTORS['compost_reduction'] if compost_food_waste else 0

# Water saving factor on showers
water_saving_factor = EMISSION_FACTORS['water_saving_factor'] if use_water_saving_fixtures else 1.0

# Shower emissions
shower_emission = showers_per_day * shower_duration_min * EMISSION_FACTORS['shower_minute'] * 365 * water_saving_factor

# Electricity emissions (annual)
electricity_emission = monthly_kwh * 12 * EMISSION_FACTORS['electricity_per_kwh']

# Total emissions
total_carbon_footprint_kgCO2 = (
    (vehicle_emission + public_transport_emission + diet_emission + aircon_emission + electricity_emission) * energy_efficiency_adj
    + clothes_emission + shower_emission - compost_reduction
)

# Show results
st.header("Your Estimated Annual Carbon Footprint (kg CO2):")
st.subheader(f"{int(total_carbon_footprint_kgCO2):,} kg CO2")

st.write("Breakdown by category:")
st.write(f"Vehicle emissions: {int(vehicle_emission):,} kg CO2")
st.write(f"Public transport emissions: {int(public_transport_emission):,} kg CO2")
st.write(f"Diet emissions: {int(diet_emission):,} kg CO2")
st.write(f"Air conditioning emissions: {int(aircon_emission):,} kg CO2")
st.write(f"Electricity emissions: {int(electricity_emission):,} kg CO2")
st.write(f"Clothing emissions: {int(clothes_emission):,} kg CO2")
st.write(f"Shower emissions: {int(shower_emission):,} kg CO2")
st.write(f"Compost reduction (subtracted): {int(compost_reduction):,} kg CO2")
