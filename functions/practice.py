# In the input, find the first A and last A, print all the letters between these two A.
# get input input_string
# create a function to find letters between first a and last a
# Problem 1
# In the input, find the first A and last A, print all the letters between these two A.

# Problem 2:
#   In the input, find the first A and last A, print all the letters between these two A. 
#   If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B. 
#   If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C.
# In the input, find the first A and last A, print all the letters between these two A. 
#   If there is no A or 2nd A is not found, find the first B after the first A (if there is a A) and last B and print all the letters between these two B. 
  
#   If there is no B or 2nd B is not found, find the first C after the first B (if there is a B) and last C and print all the letters between these two C. 
 
#defining a function with string and char
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

# if(print_between_letters(mystring,"a") != True):
    #print_between_letters(mystring,"b")
   


        