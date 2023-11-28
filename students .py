#using for loop to get name for 3 students
for student in range(1, 4):
    #getting the name of student from the user
    student_name = input(f"Enter name for Student {student}: ")
   #for loop to get 2 marks each for a student 
    for mark in range(1, 3):
        #get the marks scored by the students
        mark_scored = int(input(f"Enter Mark {mark} for {student_name}: "))
        print(f"Mark {mark} for {student_name} is {mark_scored}")
        
