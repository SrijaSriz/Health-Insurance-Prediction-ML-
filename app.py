import streamlit as st
import pandas as pd
import joblib

# Load the trained model and scaler
model = joblib.load("insurance_model.pkl")
scaler = joblib.load("scaler.pkl")

# Define expected input columns (same as model training)
expected_columns = [
    'age', 'BMI', 'Children',
    'gender_male',
    'smoking_status_yes',
    'location_northwest', 'location_southeast', 'location_southwest'
]

def main():
    st.set_page_config(page_title="Health Insurance Cost Predictor", layout="centered")
    st.title("🏥 Health Insurance Price Predictor")
    st.markdown("Enter your details to estimate the health insurance cost.")

    # Input fields
    age = st.slider("Age", 18, 64, 30)
    bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=60.0, value=25.0)
    children = st.slider("Number of Children", 0, 5, 1)
    gender = st.selectbox("Gender", ["female", "male"])
    smoking_status = st.selectbox("Smoking Status", ["no", "yes"])
    region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

    # Create input dict for one-hot encoded fields
    input_dict = {
        'age': [age],
        'BMI': [bmi],
        'Children': [children],
        'gender_male': [1 if gender == "male" else 0],
        'smoking_status_yes': [1 if smoking_status == "yes" else 0],
        'location_northwest': [1 if region == "northwest" else 0],
        'location_southeast': [1 if region == "southeast" else 0],
        'location_southwest': [1 if region == "southwest" else 0],
    }

    input_df = pd.DataFrame(input_dict)

    # Ensure all expected columns are present (add missing as 0)
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns to match training
    input_df = input_df[expected_columns]

    # Scale numerical columns
    input_df[['age', 'BMI', 'Children']] = scaler.transform(input_df[['age', 'BMI', 'Children']])

    # Predict and display result
    if st.button("Predict Insurance Price"):
        prediction = model.predict(input_df)
        st.success(f"💰 Estimated Insurance Price: ₹{prediction[0]:,.2f}")

if __name__ == "__main__":
    main()
