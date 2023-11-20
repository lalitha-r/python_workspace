# Problem #2
# you have a list of student names and another list with their marks in CS.
# hard code the values. no need to get it as input
# Pass mark is 50.
# Print a new list with all the students with pass marks along with their mark in the format name:mark.
# Also print the number of students who failed.

student_names = ['theeru', 'mithu', 'ram', 'vasee',
                 'visva']  # create a list for student name
cs_marks = [34, 78, 49, 60, 67]  # create a list for student marks in cs
pass_mark = 50  # initialise pass mark as 50
pass_list = []  # empty array for pass list
fail_list = []  # empty array for fail list
for i in range(len(student_names)):
    if cs_marks[i] >= pass_mark:  # checking for pass mark
        # add the passed students to the pass list
        pass_list.append(student_names[i] + ":" + str(cs_marks[i]))
    else:
        # add the failed students to the list
        fail_list.append(student_names[i])
print(f"the list of students passed :{pass_list}")
print(f"the number of students failed:{len(fail_list)}")

# output :
# the list of students passed :['mithu:78', 'vasee:60', 'visva:67']
# the number of students failed:2
