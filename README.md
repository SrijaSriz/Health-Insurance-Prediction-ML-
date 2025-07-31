🏥 Health Insurance Cost Predictor
An end-to-end Machine Learning project that predicts health insurance prices based on user details like age, BMI, gender, smoking status, number of children, and region. This project includes data preprocessing, feature engineering, model training, evaluation, and deployment using a Streamlit web application.

🚀 Features
Cleaned and preprocessed real-world insurance dataset

Imputation using statistical and advanced methods (mean, median, bfill)

Outlier handling using IQR and Winsorization

Feature scaling using MinMaxScaler

One-hot encoding for categorical variables

Trained multiple regression models

Final model: Random Forest Regressor

Interactive Streamlit app for real-time predictions

Exported model and scaler using joblib

📁 Project Structure
bash
Copy
Edit
health-insurance-cost-predictor/
│
├── data/                         # Raw or processed dataset
├── app.py                       # Streamlit app
├── insurance_model.pkl          # Trained ML model
├── scaler.pkl                   # MinMaxScaler object
├── EDA_and_Modeling.ipynb       # Complete notebook (EDA + Training)
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
🛠 Tech Stack
Language: Python

Libraries: pandas, numpy, seaborn, matplotlib, sklearn, joblib, streamlit

Model: RandomForestRegressor

Deployment: Streamlit App

⚙️ How to Run Locally
bash
Copy
Edit
# 1. Clone the repo
git clone https://github.com/yourusername/health-insurance-cost-predictor.git

# 2. Navigate to the project directory
cd health-insurance-cost-predictor

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
🎯 Prediction Inputs
Age (18–64)

BMI (Body Mass Index)

Children (Number of children covered)

Gender (Male / Female)

Smoking Status (Yes / No)

Region (northeast / northwest / southeast / southwest)

📈 Model Performance
Model	MAE	MSE
Linear Regression	0.0197	0.2422
Decision Tree	0.0280	0.3527
Polynomial Regression	0.0199	0.2524
Random Forest	0.0138	0.1703

✔️ Random Forest performed best and was selected as the final model.

💡 Use Case
This tool is ideal for:

Insurance providers to design personalized plans

Customers to estimate costs and plan budgets

Healthcare analytics platforms for pricing strategies

📌 License
This project is open-source and available under the MIT License.
