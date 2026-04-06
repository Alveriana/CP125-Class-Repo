import pandas as pd


def critical_inventory(data):
    df = pd.read_csv(data)

    total_products = len(df)

    critical_inventory = df[df['StockLevel'] < df['ReorderThreshold']]

    cri_inventory_set = set(critical_inventory['ProductName'])


    return {
        "total_products" : total_products,
        "critical_count" : critical_inventory,
        "critical_products" : cri_inventory_set
    }

critical_inventory("labs/lab09/data/inventory.csv")