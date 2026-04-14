import streamlit as st
import joblib
import pandas as pd

model = joblib.load("models/model.pkl")

st.title("⚙️ AI Predictive Maintenance System")

temperature = st.slider("Temperature", 0, 100, 50)
vibration = st.slider("Vibration", 0, 10, 2)
current = st.slider("Current", 0, 500, 200)

if st.button("Predict"):
    data = pd.DataFrame([[temperature, vibration, current]],
                        columns=['temperature', 'vibration', 'current'])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ Failure Likely")
    else:
        st.success("✅ Normal")