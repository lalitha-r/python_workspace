# Problem #3
# you have a list of student names. you have one list each for their marks in CS, Math and English.
# hard code the values. no need to get it as input
# Pass mark is 50.
# Grade A is, mark 90 or above
# Grade B , 80 or above
# Fail is < 50
# Print the name of the students who got A in all subjects or atleast one A and the rest B.
# Try to use only one if statement.

student_names = ['theeru', 'mithu', 'ram', 'vasee',
                 'visva']  # create a list for student name
cs_marks = [90, 78, 49, 95, 91]  # create a list for cs marks
math_marks = [89, 67, 83, 87, 98]  # create a list for maths marks
eng_marks = [83, 43, 77, 88, 97]  # create a list for english marks
for i in range(len(student_names)):  # loop that iterate over the student names
    # calculate number of students who got grade A
    calc_a = sum([cs_marks[i] >= 90, math_marks[i] >= 90, eng_marks[i] >= 90])
    calc_b = sum([80 <= cs_marks[i] < 90, 80 <= math_marks[i]  # calculate number of students who got grade B
                 < 90, 80 <= eng_marks[i] < 90])

    if calc_a == 3 or (calc_a >= 1 and calc_b >= 2) or calc_b == 3:
        print(
            f"Student with all A grades or at least one A grade and the rest B:{student_names[i]}")
#     else:
#         # Check for students who failed in any subject
#         failed = sum([cs_marks[i] < 50, math_marks[i] < 50, eng_marks[i] < 50])
#         if failed:
#             print(
#                 f"Student who failed in at least one subject:{student_names[i]}")

#  output:
# Student with all A grades or at least one A grade and the rest B:theeru
# Student with all A grades or at least one A grade and the rest B:vasee
# Student with all A grades or at least one A grade and the rest B:visva
