# Problem #2
# you have a list of student names and another list with their marks in CS. 
# hard code the values. no need to get it as input
# Pass mark is 50.
# Print a new list with all the students with pass marks along with their mark in the format name:mark.
# Also print the number of students who failed.
student_names = ['lali','mithu','theeru','jaya'] # create a list for student name
student_marks = [45,60,75,34,]# create a list for student marks
pass_mark = 50 #initialise pass mark as 50
pass_list =[] # empty array for pass list
fail_list =[] # empty array for fail list
for i in range(len(student_names)): 
    if student_marks[i] >= pass_mark:# checking for pass mark
        pass_list.append(student_names[i]+ ":"+ str(student_marks[i]))# add the passed students to the pass list
    else :
        fail_list.append(student_names[i])# add the failed students to the list
print(pass_list) 
print(f"the number of students failed:{len(fail_list)}")

# output:
# ['mithu:60', 'theeru:75']
# the number of students failed:2
