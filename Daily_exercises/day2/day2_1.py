# Problem #1
# Print the following pattern
# 1
# 212
# 32123
# 4321234
# 543212345
# Get user input for how far to go (up to 0)

# get user input for no of rows
inp = int(input("Enter the number of steps : "))

for i in range(1, inp + 1):
    # Initialize an empty string for the pattern
    pattern = ""

    # First part of the pattern decrement j by 1
    for j in range(i, 0, -1):
        pattern += str(j)

    # Second part of the pattern
    for j in range(2, i + 1):
        pattern += str(j)

    # Print the complete pattern
    print(pattern)

# output:
# 1
# 212
# 32123
# 4321234
# 543212345
