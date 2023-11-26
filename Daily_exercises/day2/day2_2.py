# Write a program that reads a passage or string and counts the occurrences of two consecutive words
# that are the same without any other specific word in between.
#  For example, count the occurrences of "apple apple" but not "apple orange apple."

# get input as a passage or string from user
text = input("Enter the passage or string: ")

# Split the text into words
words = text.split()

# Initialize a counter
count = 0

# Iterate through the words and count consecutive duplicates
for i in range(len(words) - 1):
    if words[i] == words[i + 1]:
        count += 1

# print the number of occurence
print(count)

# output:
# it was the worst of times time time time"
# 2
