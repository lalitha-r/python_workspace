#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

inputSentence = input("Enter a sentence: ")  # get input from the user
pigLatinKey = 'ay'
result = []

for word in inputSentence.split():
    if len(word) >= 1:  # Check if the word has more than one character
        firstChar = word[0]
        word = word[1:] + firstChar + pigLatinKey
    else:
        word = word + pigLatinKey  # If the word has only one character, just add 'ay' to it
    result.append(word)

# Join the words back together into a sentence
outputSentence = ' '.join(result)
print(outputSentence)

# output:

# Enter a sentence: i wrote python 
# iay roteway ythonpay


