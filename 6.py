print("My Tables")

# Loop through numbers 1 to 3
for i in range(1, 4):
    print(f"Table  {i}")
    level_choice = input("Enter 'basic', 'advanced', or 'both': ")
    
    if level_choice == "basic":
        print("Easy numbers")
        for j in range(1, 11):
            print(f"{i} * {j} = {i*j}")
    elif level_choice == "advanced":
        print("Advanced numbers")
        for j in range(11, 21):
            print(f"{i} * {j} = {i*j}")
    elif level_choice == "both":
        print("Easy numbers")
        for j in range(1, 11):
            print(f"{i} * {j} = {i*j}")
        print("Advanced numbers")
        for j in range(11, 21):
            print(f"{i} * {j} = {i*j}")
    else:
        print("Invalid choice")
    
                                                                                                                                                                                                           [l m,kivpbk,o
                                                                                                                                                                                                             ,print(f"*"*10)

# Print end of tables
print("End of tables")
