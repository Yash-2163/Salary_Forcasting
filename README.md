# 🧠 Salary Prediction ML System

An end-to-end machine learning pipeline that predicts employee salaries across various roles, regions, and companies. The project handles everything from data ingestion and model training to real-time serving, monitoring, and automated retraining.

---

## 🔧 Tech Stack

- **Python**, **Pandas**, **Scikit-learn** – Data preprocessing and model training  
- **RandomForestRegressor + RFE** – Final model with top 10 features  
- **Flask** – REST API backend to serve model  
- **Streamlit** – Frontend dashboard for user interaction  
- **MLflow** – Experiment tracking and model registry  
- **Evidently AI** – Monitoring for data and concept drift  
- **Apache Airflow** – Orchestrates daily retraining pipeline  
- **Docker** – Containerized development and deployment  

---

## 📊 Project Architecture

```plaintext
                      ┌────────────────────┐
                      │    Raw Dataset     │
                      └────────┬───────────┘
                               ↓
                ┌─────────────────────────────┐
                │     Data Preprocessing      │
                │ (normalization, feature sel)│
                └────────┬────────────┬───────┘
                         ↓            ↓
             ┌────────────────┐    ┌────────────┐
             │ Model Training │    │  MLflow    │◄────────────┐
             └──────┬─────────┘    └────────────┘             │
                    ↓                                        │
           ┌──────────────────┐     ┌────────────┐           │
           │ Flask API Server │◄───►│ Streamlit UI│           │
           └────────┬─────────┘     └────────────┘           │
                    ↓                                        │
          ┌────────────────────────────┐                    │
          │   Evidently Drift Monitor  │                    │
          └────────┬───────────────────┘                    │
                   ↓                                        │
         ┌───────────────────────────────┐                 │
         │ Apache Airflow (Daily Retrain)│─────────────────┘
         └───────────────────────────────┘
