for i in range(1, 4):
    print(f"Table  {i}")
    
    # Print easy numbers
    print("Easy numbers")
    for j in range(1, 11):
        result = i * j
        print(f"{i} * {j} = {result}")
    
    # Print advanced numbers
    print("Advanced numbers")
    for j in range(11, 21):
        result = i * j
        print(f"{i} * {j} = {result}")
    
    # Print separator line
    print(f"*"*10)

# Print end of tables
print("End of tables")





