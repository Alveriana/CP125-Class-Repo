import csv

def calculate_averages(midterm_file, final_file, output_file):

    f1 = open(midterm_file,"r",newline=)
    f2 = open(final_file,"r",newline=)

    reader1 = csv.reader.writter(f1)
    reader2 = csv.reader.writter(f2)

    next(reader1)
    next(reader2)

    midterm_score = {}
    final_score = {}

    for item in reader1:
        name = item[0]
        mark = item[1]
        midterm_score[name] = mark

    for item in reader2:
        name = item[0]
        mark = item[1]
        final_score[name] = mark

    f1.close()
    f2.close()

    f = open(output_file,"w")
    f.write("name, average\n")

    for name in midterm_score:
        if name in final_score:
            average = (midterm_score[name] + final_score[name])/2
            f.write(f"(name)")