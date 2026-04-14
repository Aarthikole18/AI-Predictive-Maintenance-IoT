import pandas as pd
import matplotlib.pyplot as plt

def plot_graphs():
    df = pd.read_csv("data/iot_data.csv")

    plt.figure()
    plt.plot(df['temperature'])
    plt.title("Temperature Trend")
    plt.savefig("images/temperature_plot.png")
    plt.show()

    plt.figure()
    df['failure'].value_counts().plot(kind='bar')
    plt.title("Failure Distribution")
    plt.savefig("images/failure_plot.png")
    plt.show()