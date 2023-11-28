print("My Tables")

# Get user input for table numbers
table_numbers_str = input("Enter a list of table numbers (comma-separated): ")
table_numbers = [int(num) for num in table_numbers_str.split(',')]

# Get user input for level choice 
level_choice = input("Enter 'basic', 'advanced', or 'both': ")

# Loop through user-specified table numbers
for i in table_numbers:
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