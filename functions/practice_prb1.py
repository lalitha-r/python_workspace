#  Problem 1
# In the input, find the first A and last A, print all the letters between these two A.

def print_between_letters(input_str, char):
    input_str = input_str.lower()  #  lowercase the string
    char = char.lower()  #  Lowercase char 
    #finding the index for first char
    first_char_index = input_str.find(char) 
    
    stringfound = False
    #  Check for first char in string
    if first_char_index >= 0:  
        #find the index for last char
        last_char_index = input_str.rfind(char)
        # checking whether the first and last char are equal
        if first_char_index != last_char_index:
            #print the sliced letters
            print(input_str[first_char_index + 1:last_char_index])
            stringfound = True
        else:
            print(f"no second '{char}' is found")
    else:
        print(f"no '{char}' is found")
    
    return stringfound

mystring = input("enter the string: ")
print_between_letters(mystring, "a")

# output:
# enter the string: abcdea
# bcde

