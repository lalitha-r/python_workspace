# Problem #2
# you have a list of student names and another list with their marks in CS. 
# hard code the values. no need to get it as input
# Pass mark is 50.
# Print a new list with all the students with pass marks along with their mark in the format name:mark.
# Also print the number of students who failed.
student_names = ['lali','mithu','theeru','jaya']
student_marks = [45,60,75,34,]
pass_mark = 50
pass_list =[]
fail_list =[]
for i in range(len(student_names)):
    if student_marks[i] >= pass_mark:
        pass_list.append(student_names[i]+ ":"+ str(student_marks[i]))
    else :
        fail_list.append(student_names[i])
print(pass_list)
print(f"the number of students failed:{len(fail_list)}")

