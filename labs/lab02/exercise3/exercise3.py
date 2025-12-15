# Lab 02 Exercise 3: Secure Vault System
# Write your code below:

def validate_entry(name, pin):
    # TODO: Implement this function
    # Return True if valid, False otherwise
    if (name == "Directory" and pin == 1122) or (name == "Security" and pin == 9900):
        return True
    else:
        return False
name = input("Enter name: ")
pin = int(input("Enter pin: "))

# Test your code here
result = validate_entry(name,pin)
print(result)
print("Testing Secure Vault System...")
