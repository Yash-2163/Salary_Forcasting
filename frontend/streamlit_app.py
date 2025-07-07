import streamlit as st
import pandas as pd
import joblib
 
# Load the trained model
model = joblib.load("../model/best_model.pkl")
 
st.title("💼 Software Salary Predictor")
 
# UI Input Fields
job_title = st.selectbox("Job Title", ["Software Engineer", "Data Scientist", "Machine Learning Engineer"])
experience_level = st.selectbox("Experience Level", ["Entry Level", "Mid Level", "Senior Level", "Executive Level"])
employment_type = st.selectbox("Employment Type", ["Full-time", "Part-time", "Contract", "Internship"])
company_size = st.selectbox("Company Size", ["Small", "Medium", "Large"])
company_location = st.selectbox("Company Location", ["USA", "India", "UK", "Germany"])  # Update based on training data
currency = st.selectbox("Currency", ["USD", "INR", "GBP", "EUR"])  # Must match training data
salary_currency = st.selectbox("Salary Currency", ["USD", "INR", "GBP", "EUR"])  # Same here
remote_ratio = st.slider("Remote Ratio (%)", 0, 100, 50)
years_experience = st.number_input("Years of Experience", min_value=0.0, step=0.5)
base_salary = st.number_input("Base Salary", min_value=0.0)
bonus = st.number_input("Bonus", min_value=0.0)
stock_options = st.number_input("Stock Options", min_value=0.0)
 
if st.button("Predict Salary"):
    input_df = pd.DataFrame([{
        "job_title": job_title,
        "experience_level": experience_level,
        "employment_type": employment_type,
        "company_size": company_size,
        "company_location": company_location,
        "currency": currency,
        "salary_currency": salary_currency,
        "remote_ratio": remote_ratio,
        "years_experience": years_experience,
        "base_salary": base_salary,
        "bonus": bonus,
        "stock_options": stock_options
    }])
 
    # Prediction
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Predicted Adjusted Total Salary: ${prediction:,.2f}")
 