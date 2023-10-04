# Problem #1
# Generate the following output using for loop. Go until g.
# a
# aba
# abacaba
# abacabadabacaba
# abacabadabacabaeabacabadabacaba

# look at the output and find the pattern. Hint - add next letter in the alphabet in each row
wrapper_str = ""
for value in range(97, ord('g') + 1):
   wrapper_str = wrapper_str + chr(value) + wrapper_str
   print(wrapper_str)

   