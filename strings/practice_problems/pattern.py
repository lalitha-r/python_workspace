# Problem #1
# Generate the following output using for loop. Go until g.
# a
# aba
# abacaba
# abacabadabacaba
# abacabadabacabaeabacabadabacaba

# look at the output and find the pattern. Hint - add next letter in the alphabet in each row
#initialising the wrapper str as empty where it holds the current string value
wrapper_str = "" 
for value in range(97, ord('g') + 1):# using an ascii value for alphabets
   wrapper_str = wrapper_str + chr(value) + wrapper_str 
   print(wrapper_str)

# output:
# a
# aba
# abacaba
# abacabadabacaba
# abacabadabacabaeabacabadabacaba
# abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba
# abacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacabagabacabadabacabaeabacabadabacabafabacabadabacabaeabacabadabacaba
