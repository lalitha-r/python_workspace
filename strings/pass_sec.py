# 1. Print the level of the password security and if the password is acceptable
#     Weak - only alphabets or only numbers or only special chars
#     Ok - at least one alphabet, one number and one special char
#     strong - at least three alphabets, two numbers and one special char
#     Very strong - same as strong, but at least 16 count

#     All passwords must be at least 8 chars long. You can use RegEx if you want.


password = input("Enter your password: ") #get input from user

# Initializing counters for alphabets, digits, and special characters
alpha_count = num_count = special_char_count = 0

# Iterate through the characters in the password
for char in password:
    if char.isalpha(): #to check whether string consists of alphabets
        alpha_count += 1
    elif char.isdigit(): # to check whether string consists of digits
        num_count += 1
    else:
        special_char_count += 1

# Check the password strength based on the criteria
if len(password) < 8:
    print("Weak: Password must be at least 8 characters long.")
elif alpha_count > 0 and num_count > 0 and special_char_count > 0: # should have atleast one alphabets,digits n char
    if len(password) >= 16:
        print("Very strong")
    else:
        print("Strong")
else:
    print("OK")


# output:

# Enter your password: lali
# Weak: Password must be at least 8 characters long.
# Enter your password: Lali@4536
# Strong