def print_between_letters(input_str, char, start_index=0):
    first_char = input_str.find(char, start_index)
    stringfound = False

    if first_char >= 0:  # Changed condition to account for char at index 0
        last_char = input_str.rfind(char)
        
        if first_char != last_char:
            print(input_str[first_char+1:last_char])
            stringfound = True
        else:
            print(f"no second {char}")
    else:
        print(f"no {char}")

    return stringfound, first_char  # Return index of the first occurrence for subsequent searches

mystring = input("enter the string")

found_a, position_a = print_between_letters(mystring, "a")
if not found_a:
    found_b, _ = print_between_letters(mystring, "b", position_a + 1)
    if not found_b:
        print_between_letters(mystring, "c")