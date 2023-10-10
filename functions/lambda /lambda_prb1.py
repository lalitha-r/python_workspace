#Write a Python program to sort a list of tuples using Lambda.
# [("apple", 50),("orange", 15) ,("mango", 30)]
# sort by name or cost

# defining a list of tuples with fruits name and its cost
input_list = [("apple", 50), ("orange", 15), ("mango", 30)]

# get the choice from the user to get name or cost
choice = input("Sort by 'name' or 'cost': ")


if choice == "name":
    sorted_list = sorted(input_list, key=lambda x: x[0])  # Sort by fruit name using lambda function
    output = [item[0] for item in sorted_list]      # get names using for loop
elif choice == "cost":
    sorted_list = sorted(input_list, key=lambda x: x[1])  # Sort by cost using lambda
    output = [item[1] for item in sorted_list]      # get costs using for loop
else:
    print("Invalid choice!")
    output = input_list # print the input if it is invalid choice
  
print(output)

# output:

# Sort by 'name' or 'cost': name
# ['apple', 'mango', 'orange']
# logesh@Logeshs-MacBook-Pro python_workspace % 
# /usr/local/bin/python3 "/Users/logesh/python_w
# orkspace/functions/lambda /lambda_prb1.py"
# Sort by 'name' or 'cost': cost
# [15, 30, 50]
# logesh@Logeshs-MacBook-Pro python_workspace % 
# /usr/local/bin/python3 "/Users/logesh/python_w
# orkspace/functions/lambda /lambda_prb1.py"
# Sort by 'name' or 'cost': jfvg
# Invalid choice!
# [('apple', 50), ('orange', 15), ('mango', 30)]
# logesh@Logeshs-MacBook-Pro python_workspace % 

