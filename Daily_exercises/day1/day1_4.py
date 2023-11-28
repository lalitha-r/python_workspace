# problem #4
# write a program to find if two strings are same.
# two string are considered same if both strings have same letters in same order, but from different starting point
# eg abcd is same as bcda (a is moved to the right)
# abcd is same as cdab
# abcd is  not same as cdba

# 123456 = 456123
# 123456 not = 412356
# hint -
# there are many simple answers. you can try with slice function

str1 = input("enter string1:")  # get input for string1
str2 = input("enter string2:")  # get input for string2

if len(str1) != len(str2):
    print("the two strings are not same")

else:
    for i in range(len(str1)):  # starts a loop that will iterate over the indices of str1
        # using slice function check whether two strings are equal
        if (str1[i:] + str1[:i] == str2):
            print("The two strings are same")

    print("the two strings are not same")


# output:
# enter string1:abcd
# enter string2:cdba
# the two strings are not same
