# Problem #3
# you have a list of student names. you have one list each for their marks in CS, Math and English. 
# hard code the values. no need to get it as input
# Pass mark is 50.
# Grade A is, mark 90 or above
# Grade B , 80 or above
# Fail is < 50
# Print the name of the students who got A in all subjects or atleast one A and the rest B.
# Try to use only one if statement.

student_names = ["Alice", "Bob", "Charlie", "David", "Eva"]

# Marks for each subject
cs_marks = [95, 85, 91, 78, 92]
math_marks = [88, 91, 93, 81, 89]
english_marks = [90, 80, 79, 92, 85]

# Loop through each student
for i in range(len(student_names)):
    a_count = sum([cs_marks[i] >= 90, math_marks[i] >= 90, english_marks[i] >= 90])
    b_count = sum([80 <= cs_marks[i] < 90, 80 <= math_marks[i] < 90, 80 <= english_marks[i] < 90])

    # Check if student got A in all subjects or at least one A and the rest B or B in all subjects
    if a_count == 3 or (a_count >= 1 and b_count >= 2) or b_count == 3:
        print(student_names[i])