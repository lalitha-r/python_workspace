# Problem 1
# Print the following pattern
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1

# Observe how the nunmbers in the triangle are calculated.
# Do it in two steps. Work on the generating the numbers first in right angle triangle
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

# And then work on the final output using proper indendation

# initialize the num of rows
n = 5

# Printing the first row separately
print("1")

# For the remaining rows
for i in range(1, n):
    row = [1]  # First element of each row is always 1
    if i > 1:
        # Calculate middle elements of the row
        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])
    row.append(1)  # Last element of each row is always 1
    prev_row = row  # Update the previous row

    # Print the current row
    for num in row:
        print(num, end=' ')
    print()

    n = 5

# Printing the triangle with indentation
for i in range(n):
    # Print leading spaces
    print(' ' * (n - i - 1), end='')

    # First element of each row is always 1
    num = 1
    for j in range(1, i + 2):
        print(num, end=' ')

        # Calculate the next number in the row
        num = num * (i - j + 1) // j

    # Move to the next line after each row
    print()


n = 5

# Printing the right-angle triangle
for i in range(n):
    # First element of each row is always 1
    num = 1
    for j in range(1, i + 2):
        print(num, end=' ')

        # Calculate the next number in the row
        num = num * (i - j + 1) // j

    # Move to the next line after each row
    print()
# output:

# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
