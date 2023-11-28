# Problem 1:
# Write a program to calculate your avg marks in CS subject in the last 3 exams.
def calculate_avg() :
    marks = []
    for i in range (5) :
        mark = float(input(f"enter the mark for cs subject in exam{i+1}:"))
        marks.append(mark)
    
    last_3_marks = marks[-3:]
    avg = sum(last_3_marks)/ 3

    print (f"the average mark for last 3 exams are {avg}:")
calculate_avg()


    