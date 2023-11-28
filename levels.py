print("My Tables")

# Loop through numbers 1 to 3
for i in range(1, 4):
    level_choice = input("Enter 'basic', 'advanced','both': ")
    if level_choice == "basic":
        print("Easy numbers")
        for j in range(1, 11):
            result = i * j
            print(f"{i} * {j} = {result}")
    elif level_choice == "advanced":
        print("Advanced numbers")
        for j in range(11, 21):
            result = i * j
            print(f"{i} * {j} = {result}")
    else:
        print("Invalid choice")
    
    print(f'*'*11)

# Print end of tables
print("End of tables")

