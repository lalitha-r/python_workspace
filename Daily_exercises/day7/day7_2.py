
# Problem 2:
#   In the input, find the first A and last A, print all the letters between these two A.
#   If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B.
#   If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C.


def find_first_char(input_string, char):
    return input_string.lower().find(char)


def find_last_char(input_string, char):
    return input_string.lower().rfind(char)


def letters_between_char(input_string, char):
    first_char = find_first_char(input_string, char)
    last_char = find_last_char(input_string, char)

    if first_char != -1 and last_char != -1:
        return input_string[first_char + 1:last_char]
    else:
        return None


def main():
    input_string = input("Enter a string: ")
    char = input("Enter the character: ")
    output = letters_between_char(input_string, char)

    if output:
        print(f"Letters between the first '{char}' and last '{char}':", output)
    else:
        print(f"No '{char}' found in the input string.")


if __name__ == "__main__":
    main()
