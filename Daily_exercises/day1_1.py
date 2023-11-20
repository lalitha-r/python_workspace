# Problem #1
# Generate the following output using for loop. Go until g.
# a
# aba
# abacaba
# abacabadabacaba
# abacabadabacabaeabacabadabacaba
# look at the output and find the pattern. Hint - add next letter in the alphabet in each row

input_str = ""  # initialize the input str as empty
# use for loop to iterate using ascii values for lowercase alphabets
for value in range(97, 105):
    # concatinate the str according to the pattern.chr(values) return its alphabets
    input_str = input_str + chr(value) + input_str
    print(input_str)  # print the output


# output:
# a
# aba
# abacaba
# abacabadabacaba
# abacabadabacabaeabacabadabacaba
# abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba
# abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacabagabacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba
# abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacabagabacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacabahabacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacabagabacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba
