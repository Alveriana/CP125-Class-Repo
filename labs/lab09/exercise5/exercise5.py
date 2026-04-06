import pandas as pd


def high_performers(data):
    df = pd.read_csv(data)

    high_performers = df[(df['Math']>85) & (df['Science']>85) & (df['English']>85)]

    #return name as set
    names_set = set(high_performers['Name'])

    return {
        "count" : len(names_set),
        "names" : names_set
    }

high_performers("labs/lab09/data/students.csv")