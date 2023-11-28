# problem #5
# In your college Python is taught in 3 different departments by the same professor.
# For each dept, get the no of students studying Python and their marks in the final exam
# Get the input as comma seperated string

# Find the top 3 marks in each class
# Find the top 3 marks in all classes are combined.
# Find the avg mark of students with passing mark in each class and the classes combined.
# Find which class has the best average mark and least number of failed students.

# get input for no of students in 3 diff dept
stu_it = int(input("enter the number of students in IT dept:"))
stu_cs = int(input("enter the number of students in CS dept:"))
stu_ece = int(input("enter the number of students in ECE dept:"))

# get input for marks in each class
mark1 = input(
    f"enter the marks for {stu_it} IT  students as comma separated:").split(',')
mark2 = input(
    f"enter the marks for {stu_cs} CS students as comma separated:").split(',')
mark3 = input(
    f"enter the marks for {stu_ece} ECE students as comma separated:").split(',')

# convert marks from string to integer
marks_it = [int(mark) for mark in mark1]
marks_cs = [int(mark) for mark in mark2]
marks_ece = [int(mark) for mark in mark3]

# calculate top 3 marks in each class
top_it = sorted(marks_it)[-3:]
top_cs = sorted(marks_cs)[-3:]
top_ece = sorted(marks_ece)[-3:]

# calculate top 3 marks in all class combined
top_allclass = sorted(marks_it + marks_cs + marks_ece)[-3:]

# calculate avg mark of students with passing mark in each class
passing_mark = 50
avg_it_passing = sum([mark for mark in marks_it if mark >= passing_mark]) / \
    len([mark for mark in marks_it if mark >= passing_mark])
avg_cs_passing = sum([mark for mark in marks_cs if mark >= passing_mark]) / \
    len([mark for mark in marks_cs if mark >= passing_mark])
avg_ece_passing = sum([mark for mark in marks_ece if mark >= passing_mark]) / \
    len([mark for mark in marks_ece if mark >= passing_mark])

# calculate avg mark of passing students in all class
overall_avg = (avg_it_passing + avg_cs_passing + avg_it_passing)/3
