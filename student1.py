for student in range(1, 4):
    student_name = input(f"Enter name for Student {student}: ")
    
    # Initialize variables to store marks
    mark1 = int(input(f"Enter Mark 1 for {student_name}: "))
    mark2 = int(input(f"Enter Mark 2 for {student_name}: "))
    
    # Print the output for each student
    print(f"{student_name}'s marks {mark1}, {mark2}")