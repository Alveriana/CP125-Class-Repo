def show_menu():
    print("\n--- COOPMART Inventory Management ---")
    print("1. Add item")
    print("2. Delete item")
    print("3. Search item")
    print("4. Show inventory")
    print("5. Exit")


inventory = {}
running = True

while running:
    show_menu()
    choice = int(input("Enter your choice (1-5): "))

    # Validate menu choice
    if choice < 1 or choice > 5:
        print("Error: Invalid choice. Please enter a number between 1 and 5.")

    elif choice == 1:
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))

        if quantity < 0:
            print("Error: Quantity cannot be negative.")
        else:
            if item in inventory:
                inventory[item] += quantity
                print(f"Item '{item}' already exists. Quantity updated to {inventory[item]}.")
            else:
                inventory[item] = quantity
                print(f"Item '{item}' added.")

    elif choice == 2:
        if not inventory:
            print("Inventory is empty.")
        else:
            item = input("Enter item name to delete: ")
            if item not in inventory:
                print(f"Error: Item '{item}' not found.")
            else:
                del inventory[item]
                print(f"Item '{item}' removed.")

    elif choice == 3:
        if not inventory:
            print("Inventory is empty.")
        else:
            item = input("Enter item name to search: ")
            if item not in inventory:
                print(f"Error: Item '{item}' not found.")
            else:
                print(f"Quantity of '{item}': {inventory[item]}")

    elif choice == 4:
        if not inventory:
            print("Inventory is empty.")
        else:
            print("\nInventory:")
            for item, quantity in inventory.items():
                print(f"{item}: {quantity}")

    elif choice == 5:
        print("Goodbye!")
        running = False
