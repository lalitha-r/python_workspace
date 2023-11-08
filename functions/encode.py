#  You have a message that you want to send to your friend. You don't want others to see
#  the message. You code the message and send it.The alg to code is - split each word in half
# and reverse it (eg cricket becomes ketccri), if the word ends with a vowel, split at the last
# letter and reverse (eg cinema becomes acinem), if the word has numbers, spell the number but add
# A as first and last letters

# splitting each word in half and reverse
def split_word_and_reverse(word):
    # find the length of the word
    word_length = len(word)
    # split the word
    half_length = word_length // 2

    first_half = word[:half_length]
    second_half = word[half_length:]
    # reverse the two half and concatenate them
    reversed_word = second_half[::-1] + first_half[::-1]

    return reversed_word


def split_reverse_if_vowel(word):
    # Define a list of vowels
    vowels = 'aeiou'

    # Check if the last letter of the word is a vowel
    if word[-1] in vowels:
        # Split at the last letter
        part1 = word[:-1]  # All of the word except the last letter
        part2 = word[-1]   # Just the last letter

        # Reverse the two parts and concatenate them
        new_word = part2 + part1
    else:
        # If the word does not end with a vowel, leave it as it is
        new_word = word

    return new_word


# convert numbers to words
def number_to_word(word):
    spelled_out = ''
    # use for loop to check whether the char is digit
    for char in word:
        # replace digit 0 to 9 by its name
        if char.isdigit():
            if char == '0':
                spelled_out += 'zero'
            elif char == '1':
                spelled_out += 'one'
            elif char == '2':
                spelled_out += 'two'
            elif char == '3':
                spelled_out += 'three'
            elif char == '4':
                spelled_out += 'four'
            elif char == '5':
                spelled_out += 'five'
            elif char == '6':
                spelled_out += 'six'
            elif char == '7':
                spelled_out += 'seven'
            elif char == '8':
                spelled_out += 'eight'
            elif char == '9':
                spelled_out += 'nine'
        else:
            spelled_out += char

    # If we spelled out any numbers, we add 'A' at the beginning and end of the string.
    if spelled_out != word:
        spelled_out = 'A' + spelled_out + 'A'

    return spelled_out


def encode_message(message):
    # Split the message into words
    words = message.split()

    encoded_words = []

    for word in words:
        # Step 1: Split each word in half and reverse it
        reversed_word = split_word_and_reverse(word)
        # print(reversed_word)

        # convert number to words
        num_to_word = number_to_word(reversed_word)
        # split and reverse if word contains vowel at its end
        vowel_reversed_word = split_reverse_if_vowel(num_to_word)

        encoded_words.append(num_to_word)

    # print(encoded_words)
    encoded_message = ' '.join(encoded_words)

    return encoded_message


# Example usage:
message = "I love playing football and watching movies in 2023"
result = encode_message(message)
print(result)


# output:
# logesh@Logeshs-MacBook-Pro python_workspace % /usr/local/bin/python3 /Users/logesh/python_workspace/functions/enc
# ode.py
# I evol gniyalp llabtoof dna gnihctaw seivom ni AthreetwozerotwoA
