⚙️ AI-Powered Predictive Maintenance for IoT Devices

🚀 Project Overview

This project is an AI-based Predictive Maintenance System that uses machine learning to predict machine failures based on IoT sensor data like temperature, vibration, and current.

It helps industries prevent machine breakdowns before they occur, reducing downtime and maintenance cost.

🎯 Problem Statement

Machines often fail without warning, causing:

Production loss
High maintenance cost
System downtime

This project solves that using Machine Learning prediction models.

🧠 Features
Real-time failure prediction
IoT sensor data simulation
Machine Learning model (Random Forest)
Data visualization (graphs)
Streamlit UI for live prediction

🛠️ Tech Stack
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Streamlit
Joblib

📊 Dataset

Simulated IoT sensor dataset:

Temperature
Vibration
Current
Failure label (0/1)

🏗️ Project Workflow
Data Collection (Simulated IoT sensors)
Data Preprocessing
Model Training (Random Forest)
Prediction Engine
Visualization
Streamlit UI Deployment

▶️ How to Run
pip install -r requirements.txt

Run model:

python main.py

Run UI:

streamlit run app.py

🌐 Future Improvements
Real IoT hardware integration
Cloud deployment (AWS/Azure)
Deep Learning (LSTM model)
Real-time sensor streaming
