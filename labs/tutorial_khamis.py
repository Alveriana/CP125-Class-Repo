def calculate_average(score1, score2, score3):
    avg = (score1 + score2 + score3) / 3
    return avg
# Now use it for all students
print("Student 1:", calculate_average(80, 90, 85))
print("Student 2:", calculate_average(75, 88, 92))
print("Student 3:", calculate_average(95, 87, 90))
print()

# Process 5 student scores
total = 0
highest = 0
pass_count = 0

for i in range(5):
    score = int(input(f"Enter score {i+1}: "))
    total = total + score

    if score > highest:
        highest = score

    if score >= 50:
        pass_count = pass_count + 1

average = total / 5
pass_rate = (pass_count / 5) * 100

print(f"Average: {average}")
print(f"Highest: {highest}")
print(f"Pass rate: {pass_rate}%")
print()

# Process 5 student scores
def process_score(num_student, pass_score):
    highest = 100
    total = 0
    highest_score = 0
    pass_count = 0

    for i in range(num_student):
        score = int(input(f"Enter score {i+1}: "))
        total = total + score

        if score > highest_score:
            highest_score = score

        if score >= pass_score:
            pass_count = pass_count + 1

average = total / 5
pass_rate = (pass_count / 5) * 100

print(f"Average: {average}")
print(f"Highest: {highest}")
print(f"Pass rate: {pass_rate}%")
print()