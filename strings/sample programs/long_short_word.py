# 2. From a given passage find the longest and shortest word
# and print the same. Accept the passage as an input from user
# try to incorporate error handling feature too in all the
# above problems.

import re

# Accept the passage from the user
passage = input("Enter the passage: ")

try:
    # Use regular expressions to extract words from the passage
    words = re.findall(r'\b\w+\b', passage)

    # If no words are found, raise a ValueError
    if not words:
        raise ValueError("No words found in the provided passage.")

    # Find the longest and shortest words using the max and min functions with len as the key
    longest_word = max(words, key=len)
    shortest_word = min(words, key=len)

    # Print the results
    print(f"Longest word: {longest_word}")
    print(f"Shortest word: {shortest_word}")

except Exception as e:
    print(f"An error occurred: {e}")
