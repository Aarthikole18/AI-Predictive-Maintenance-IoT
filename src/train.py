import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    df = pd.read_csv("data/iot_data.csv")

    X = df[['temperature', 'vibration', 'current']]
    y = df['failure']

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, "models/model.pkl")

    print("✅ Model trained and saved!")