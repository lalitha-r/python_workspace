input_str = input("Enter a sentence: ")

# Convert the string to lowercase to ignore case
input_str = input_str.lower()

# Initialize a list to count the occurrences of each letter
letter_counts = [0] * 26  # Assuming only lowercase letters are counted

# Count the occurrences of each letter in the string
for char in input_str:
    if 'a' <= char <= 'z':
        index = ord(char) - ord('a')
        letter_counts[index] += 1

# Create a list to store letters
letters = []
for i in range(26):
    letters.append(chr(ord('a') + i))

# Sort the letters by their frequencies (descending) and then by letter (ascending)
sorted_letters = sorted(letters, key=lambda x: (-letter_counts[ord(x) - ord('a')], x))

# Initialize an empty result string
r
