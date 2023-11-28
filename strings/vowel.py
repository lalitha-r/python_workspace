#PigLatin - From the input string, for each word, remove the first chars until a vowek, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay (in Python 'o' is the first vowel)

inputSentence = input("Enter a sentence: ")  # get input from user
pigLatinKey = 'ay' #assign 'ay' value to the variable
vowels = ['a', 'e', 'i', 'o', 'u'] #initialize the vowels

result = [] #creating an empty array 

for word in inputSentence.split(' '):
    first_vowel_index = 0
    for index, char in enumerate(word):
        if char.lower() in vowels:  # Check if the character is a vowel
            first_vowel_index = index
            break

    if first_vowel_index > 0:  # Check if there is a vowel in the word
        word = word[first_vowel_index:] + word[:first_vowel_index] + pigLatinKey
    else:
        word = word + pigLatinKey  # If there are no vowels, just add 'ay' to the end

    result.append(word)

# Joining the words back together into a sentence
outputSentence = ' '.join(result)
print(outputSentence)






