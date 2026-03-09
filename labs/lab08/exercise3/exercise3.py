# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:
import csv

def calculate_order_total(products_file, order_file, output_file):
    """
    Calculate total cost for each product in order.

    Args:
        products_file: path to products CSV (product_id,product_name,price)
        order_file: path to order CSV (product_id,quantity)
        output_file: path to output CSV file

    Returns:
        float: grand total of all orders
    """
    # TODO: Implement this function
    item_prices = {}
    product =  open(products_file, "r", newline="")
    reader = csv.reader(product)
    next(reader)

    #open in data/product.csv
    for row in reader:
        product_id = row[0]
        price = float(row[2])
        item_prices[product_id] = float(price)

    product.close()

    total_cost = 0

    order = open(order_file, "r", newline="")
    reader = csv.reader(order)
    next(reader)

    output = open(output_file, "w", newline="")
    writer = csv.writer(output)
    writer.writerow(["product_id", "total_cost"])

    grand_total = 0
    #open in data/order.csv
    for row in reader:
        product_id = row[0]
        quantity = int(row[1])
        
        total_cost = item_prices[product_id] * quantity
        writer.writerow([product_id, f"{total_cost:.2f}"])
        grand_total += total_cost
    
    order.close()
    output.close()

    return grand_total
        

# Test your code here
result = calculate_order_total("labs/lab08/exercise3/data/products.csv", "labs/lab08/exercise3/data/order.csv", "labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")
