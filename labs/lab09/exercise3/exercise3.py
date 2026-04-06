import pandas as pd
import matplotlib.pyplot as plt


def show_math_trend(data):
    df = pd.read_csv(data)

    plt.plot(df.index, df['Math'])

    plt.xlabel("Student Index")
    plt.ylabel("Math Score")
    plt.title("Math Score Trends")

    plt.show()

    return len(df)

show_math_trend("labs/lab09/data/students.csv")