import joblib
import pandas as pd

def predict(data):
    model = joblib.load("models/model.pkl")

    df = pd.DataFrame([data], columns=['temperature', 'vibration', 'current'])

    prediction = model.predict(df)

    if prediction[0] == 1:
        return "⚠️ Machine Failure Likely"
    else:
        return "✅ Machine Running Normally"