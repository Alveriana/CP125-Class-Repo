# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    """
    Filter students with passing scores (>= 80) and write to output file.

    Args:
        input_file: path to input file (student_id and score on alternating lines)
        output_file: path to output file

    Returns:
        int: count of passing students
    """
    # TODO: Implement this function
    passing_count = 0
    passing_students = []

    f = open("labs/lab08/exercise1/data/scores.txt", "r")

    for i in range ()


# Test your code here
result = filter_passing_scores("data/scores.txt", "data/passing.txt")
print(f"Passing students: {result}")
