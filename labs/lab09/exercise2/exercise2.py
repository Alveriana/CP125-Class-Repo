import pandas as pd

def compare_averages(data):
    df = pd.read_csv(data)

    math_average = round(df['Math'].mean(), 1)
    science_average = round(df['Science'].mean(), 1)
    eng_average = round(df['English'].mean(), 1)

    average = {
        "Math" : math_average,
        "Science" : science_average,
        "English" : eng_average
    }

    best_subject = max(average, key=average.get)
    worst_subject = min(average, key=average.get)

    return {
        "Math" : math_average,
        "Science" : science_average,
        "English" : eng_average,
        "best_subject" : best_subject,
        "worst_subject" : worst_subject
    }