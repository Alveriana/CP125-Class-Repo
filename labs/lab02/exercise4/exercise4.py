# Lab 02 Exercise 4: Dynamic Parking Rate
# Write your code below:

def get_hourly_rate(vehicle_type, hour_24):
    # TODO: Implement this function
    # Return hourly rate based on vehicle and time
    if vehicle_type == "Electric":
        return 2.0
    elif vehicle_type == "Hybrid":
        if hour_24 >= 22 or hour_24 <= 6:
            return 2.0
        else:
            return 5.0
    else:
        return 5.0

# Test your code here
print("Testing Dynamic Parking Rate...")
