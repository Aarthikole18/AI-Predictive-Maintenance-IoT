from src.train import train_model
from src.predict import predict
from src.visualize import plot_graphs

train_model()

sample = [75, 4, 320]
result = predict(sample)

print("Prediction:", result)

plot_graphs()