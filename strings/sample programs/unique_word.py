# 1. From a given passage extract unique words and print them.
# Accept the passage as an input from the user
# try to incorporate error handling feature too in all the
# above problems.
import re

# Accept the passage from the user
passage = input("Enter the passage: ")

try:
    # Convert the entire passage to lowercase
    passage = passage.lower()

    # Use regular expressions to extract words from the passage
    words = re.findall(r'\b\w+\b', passage)

    # Convert the list of words to a set to get unique words
    unique_words = set(words)

    # Print the unique words
    for word in sorted(unique_words):
        print(word)

except Exception as e:
    print(f"An error occurred: {e}")
