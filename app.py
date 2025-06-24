import streamlit as st

# Emission factors for different meats (kg CO2 per 100g)
EMISSION_FACTORS_MEAT = {
    "Beef": 27,
    "Pork": 12,
    "Chicken": 6,
    "Fish": 8,
    "None": 0,
}

# ... rest of your code ...

st.subheader("Diet - Meat Consumption")

meat_type = st.selectbox("Select type of meat you consume", list(EMISSION_FACTORS_MEAT.keys()))
red_meat_servings_per_week = st.slider("How many servings of this meat do you eat per week?", 0, 14, 3)
serving_size_grams = st.number_input("Average serving size (grams)", min_value=50, max_value=500, value=100)

# Calculate diet emissions using selected meat type
selected_factor = EMISSION_FACTORS_MEAT[meat_type]
diet_emission = (red_meat_servings_per_week * serving_size_grams / 100) * selected_factor * 52  # annual

# ... continue with other inputs and calculations ...
