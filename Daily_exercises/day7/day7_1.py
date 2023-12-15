# Problem 1
# In the input, find the first A and last A, print all the letters between these two A.

# without using functions

# get input from user
input_string = input("Enter a string: ")

# Find the first 'A' and last 'A'
first_a = input_string.lower().find('a')
last_a = input_string.lower().rfind('a')

if first_a != -1 and last_a != -1:
    # Extract letters between the first 'A' and last 'A'
    letters_between_a = input_string[first_a + 1:last_a]

    # Print the letters between the first 'A' and last 'A'
    print("Letters between the first 'A' and last 'A':", letters_between_a)
else:
    print("No 'A' found in the input string.")


# using functions
# function to find first 'A'
def find_first_a(input_string):
    return input_string.lower().find('a')
# functio to find second 'A'


def find_last_a(input_string):
    return input_string.lower().rfind('a')

# function to get letters between first 'A' and last 'A'


def letters_between_a(input_string):
    first_a = find_first_a(input_string)
    last_a = find_last_a(input_string)

    if first_a != -1 and last_a != -1:
        return input_string[first_a + 1:last_a]
    else:
        return None
# main function


def main():
    input_string = input("Enter a string: ")
    output = letters_between_a(input_string)

    if output:
        print("Letters between the first 'A' and last 'A':", output)
    else:
        print("No 'A' found in the input string.")


if __name__ == "__main__":
    main()
