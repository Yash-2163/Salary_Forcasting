# 💼 Instilit – Global Software Salary Intelligence Platform
 
This repository presents **Instilit**, an end-to-end solution for predicting and monitoring software professionals’ compensation across regions and experience levels. The project demonstrates a modern MLOps workflow combining model training, explainability, drift detection, API deployment, and orchestration.
 
---
 
## 🌟 Objective
 
To build a **scalable salary prediction system** capable of:
- Cleaning and standardizing raw compensation data
- Training and selecting the best regression model
- Tracking experiments and metrics
- Monitoring data and prediction drift over time
- Deploying a REST API for integration
- Providing a user interface for batch predictions
- Automating workflows using Airflow
 
---
 
## 📂 Dataset Overview
 
**File:** `Software_Salaries.csv`
 
**Key columns:**
- `job_title`
- `experience_level`
- `employment_type`
- `company_size`
- `company_location`
- `remote_ratio`
- `salary_currency`
- `years_experience`
- `base_salary`
- `bonus`
- `stock_options`
- `adjusted_total_usd` (Target variable)
 
---
 
## 🔄 Workflow Summary
 
### 🧹 Data Preparation
- Normalized inconsistent job titles.
- Filled missing categorical fields.
- Removed outliers.
- Selected `adjusted_total_usd` as the prediction target.
 
---
 
### 🧠 Model Training & Selection
Trained and evaluated:
- Linear Regression
- Random Forest Regressor
- XGBoost Regressor
 
Metrics:
- R² Score
- MAE
- MSE
 
The best model saved as `best_model.pkl`.
 
---
 
### 📈 Experiment Tracking
Used **MLflow** to log parameters, metrics, and artifacts.
![image](https://github.com/user-attachments/assets/85466841-577e-4b34-8abf-efe28b0b6d0e)
![image](https://github.com/user-attachments/assets/66445b8e-d588-443d-84df-38d5ceec0a23)


 
---
 
### 🧩 Model Explainability
SHAP was used to visualize feature importance.
 
---
 
### 🛡️ Drift Monitoring
Evidently AI generated:
- Data Drift Reports
- Model Drift Reports
- Concept Drift Reports
 
---
 
### 💻 Streamlit Web Application
Dark-themed UI for batch predictions and result download.
![image](https://github.com/user-attachments/assets/4d1b1279-124b-42e1-a051-2de09590a404)

 
---
 
### 🌐 REST API Deployment
Flask API to serve predictions via JSON.
 
---
 
### ⚙️ Workflow Orchestration
Airflow DAG automating retraining and reporting.
 
---
 
## 🚀 Getting Started
 
### Install Dependencies
```bash
pip install -r requirements.txt
