#Programmer's name: Alveriana Mohan, C02
#Problem description: Print number in ascending order, calculate sum, print the largest number

def accept_number():
    numbers = []

    for item in range(1,6):
        num = int(input(f"Enter number {item}: "))
        numbers.append(num)

    sort = sorted(numbers)
    print(f"Numbers in ascending order: {sort}")

    total_sum = sum(numbers)
    print(f"Sum of all numbers: {total_sum}")

    largest = max(numbers)
    print(f"Largest number: {largest}")

accept_number()