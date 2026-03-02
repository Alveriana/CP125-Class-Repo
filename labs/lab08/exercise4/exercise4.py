# Lab 08 Exercise 4: Student Grade Calculator
# Write your code below:
import csv

def calculate_final_grades(input_file, output_file):
    """
    Calculate final grades from midterm and final scores.

    Args:
        input_file: path to scores CSV (student_id,midterm,final)
        output_file: path to output CSV file

    Returns:
        float: average of all final grades
    """
    # TODO: Implement this function
    f = open(input_file, "r", newline="")
    reader = csv.reader(f)

    result = []
    total_mark = 0
    count = 0

    for row in header:
        if row[0] != "student_id"


        final_grade = (midterm * 0.4) + (final * 0.6)
        total += final_grade
        count += 1
        





        return total/count

# Test your code here
result = calculate_final_grades("data/scores.csv", "data/grades.csv")
print(f"Average final grade: {result:.2f}")
