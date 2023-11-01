def recursive_sum(numbers):
    if not numbers:  # If the list is empty, return 0
        return 0
    else: # Add the first number to the sum of the rest of the list
        return numbers[0] + recursive_sum(numbers[1:])

numbers = [1, 2, 3, 4, 5]
result = recursive_sum(numbers)
print("The sum of the numbers is:", result)