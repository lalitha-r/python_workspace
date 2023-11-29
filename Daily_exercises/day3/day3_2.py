# Read a passage from a file.
# Count the number of times the word 'the' followed by another 'the' without 'a' in between.

# Eg The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day.

# answer is 4 (The king, the forest, The King the next).

# For problem 2 and 3,
# Make sure your code includes exception handling for reading from a file.
# Reading material for exception handling

# open a text file in read mode


try:
    # open the text file in read mode
    with open('/Users/logesh/python_workspace/text_file.txt', 'r') as file:
        text = file.read()

    # split into words
    words = text.split()

    # Initialize a count variable to keep track of occurrences
    count = 0

    for i in range(len(words) - 1):
        if words[i].lower() == 'the':
            # Flag to track whether 'a' is found between 'the'
            found_a = False
            for j in range(i + 1, len(words) - 1):
                if words[j].lower() == 'the':
                    break  # Exit the inner loop when we find the next 'the'
                if 'a' in words[j].lower():
                    found_a = True
            if not found_a:
                count += 1

    print(f"'a' is not present between 'the' {count} times.")
except Exception as e:
    print(f"An error occurred: {e}")

# output:
# 'a' is not present between 'the' 4 times.
