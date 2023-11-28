print("My Tables")
# Loop through numbers 1 to 3
for i in range(1, 4):
    # Print the table header
    print(f"Table  {i}")
    
     # Loop through values 1 to 5 for each number
    for j in range(1, 6):
        result = i * j
        print(f"{i} * {j} = {result}")
        
    # Print the separator line
   print(f'*'*11)
    

# Print the end of tables
print("End of tables")