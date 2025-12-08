# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    # Calculate round trip distance
    total_distance = one_way_km * 2
    
    # Fuel needed for the trip
    liters_needed = total_distance / km_per_liter
    
    # Total fuel cost
    total_cost = liters_needed * price_per_liter
    
    # Return True if budget is enough
    if total_cost <= budget:
        return "Sufficient"
    else:
        return "Insufficient"

# Test your code here
print("Testing Road Trip Budgeter...")
print(is_budget_sufficient(500, 50, 2.00, 50))
