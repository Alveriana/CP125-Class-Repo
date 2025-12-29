# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    # TODO: Implement this function
    # Calculate total cost for tents and meals
    total_tent = math.ceil(participants / tent_capacity)
    tent_cost = total_tent * tent_price
    food_cost = meal_price * participants
    total_cost = tent_cost + food_cost

    return total_cost

# Test your code here
print("Testing Camping Logistics...")
print(calculate_event_cost(10, 4, 25, 15))