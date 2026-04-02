#Alveriana, C02
#Lab Test 3

import csv

#Calculate and print average
def calculate_average():
    f = open("labs/bmi.csv", "r")
    reader = csv.reader(f)

    total_height = 0
    count = 0

    next(reader)
    for row in reader:
        print(row)
        total_height += float(row[1])
        count += 1

    average = total_height / count
    print("Average Height: " , average)
    f.close()

#Adding data
def add_data():
    gender = input("Enter your gender: ")
    height = input("Enter your height: ")
    weight = input("Enter your weight: ")
    bmi = input("Enter your BMI: ")

    f = open("labs/bmi.csv", "a", newline="")
    writer = csv.writer(f)
    writer.writerow([gender, height, weight, bmi])

    f.close()

#Read again before verifying that the new row has been succesfully added
    f = open("labs/bmi.csv", "r")
    reader = csv.reader(f)

    print("\n" + "Updated Row")
    for row in reader:
        print(row)

    f.close

calculate_average()
add_data()