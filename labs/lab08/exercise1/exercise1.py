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

    input = open(input_file, "r")
    data = input.readlines()
    output = open(output_file, "w")

    for i in range (0, len(data)-1, 2):
        student_id = data[i].strip()
        score = int(data[i+1].strip())

        if score >= 80:
            output.write(student_id + " " + str(score) + "\n")
            passing_count += 1
    
    input.close()
    output.close()

    return passing_count

# Test your code here
result = filter_passing_scores("labs/lab08/data/scores.txt", "labs/lab08/data/passing.txt")
print(f"Passing students: {result}")
