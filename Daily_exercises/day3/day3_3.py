# Problem #3
# From the same file as above, read from the file, count the number of unique 4 letter words and it no of occurrences
# for each word. Write this information at the end of file under the heading "Summary of 4 letter words"

# open a text file in read mode
with open('/Users/logesh/python_workspace/text_file.txt', 'r') as file:
    text = file.read()
# split into words
words = text.split()

# create a empty dic to store the four letter word and its occurence
four_letter_words = {}

for word in words:
    if len(word) == 4:
        # Convert to lowercase to count words case-insensitively
        word = word.lower()
        if word in four_letter_words:
            four_letter_words[word] += 1
        else:
            four_letter_words[word] = 1

# Append the summary to the file
with open('/Users/logesh/python_workspace/text_file.txt', 'a') as file:
    file.write("\n\nSummary of 4 letter words:\n")
    for word, count in four_letter_words.items():
        file.write(f"{word}: {count} occurrences\n")

# output:
# The king went to the forest with the wife and a servernt. The king shot a deer. The king went to the forest again the next day.


# Summary of 4 letter words:
# king: 3 occurrences
# went: 2 occurrences
# with: 1 occurrences
# wife: 1 occurrences
# shot: 1 occurrences
# next: 1 occurrences
# day.: 1 occurrences
