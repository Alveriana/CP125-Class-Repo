#Alveriana
#Check students' grade based on mark

def determine_grade (mark):
    if mark >= 80:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"

mark = float(input("Enter the student's mark: "))
grade = determine_grade (mark)

print ("Mark: ", mark, "Grade: ", grade)
    