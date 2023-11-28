# 3. Write the function mostFrequentLetters(s), that takes a string s, and ignoring case
# (so "A" and "a" are treated the same), returns a lowercase string containing the letters of s in most frequently used order.
# (In the event of a tie between two letters, follow alphabetic order.)
# Eg - "We Attack at Dawn" is input. Output should be 'atwcdekn'
# Do not use dictionaries. Try to use string built in functions.
# Input string
s = "We Attack at Dawn"

# Convert the string to lowercase and filter out non-alphabetical characters
s = ''.join(filter(str.isalpha, s.lower()))

# Sort the characters alphabetically
s_sorted = ''.join(sorted(s))
print(s_sorted)

# Create lists to store the frequencies and characters
freqs = []
chars = []

# Loop through the unique characters in the sorted string
for char in sorted(set(s_sorted)):
    freq = s_sorted.count(char)
    freqs.append(freq)
    chars.append(char)


# Sort characters by frequency (and break ties alphabetically)
for i in range(len(chars)):
    for j in range(i + 1, len(chars)):
        if freqs[i] < freqs[j] or (freqs[i] == freqs[j] and chars[i] > chars[j]):
            freqs[i], freqs[j] = freqs[j], freqs[i]
            chars[i], chars[j] = chars[j], chars[i]

# Join characters to form the result string
result = ''.join(chars)

# Print the result
print(result)  # Expected output: 'atwcdekn'
