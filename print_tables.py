print("My Tables")

# Get user input for table numbers
table=[]
table= input("Enter the table numbers : ")
for numbers in range(table):

# Get user input for level choice
    level_choice = input("Enter 'basic', 'advanced', or 'both': ")

# Loop through user-specified table numbers
    for i in numbers:
        print(f"Table  {i}")
    
        if level_choice == "basic" or level_choice == "both":
            print("Easy numbers")
            for j in range(1, 11):
                print(f"{i} * {j} = {i*j}")
    
        if level_choice == "advanced" or level_choice == "both":
            print("Advanced numbers")
            for j in range(11, 21):
                print(f"{i} * {j} = {i*j}")
    
    print(f"*"*10)