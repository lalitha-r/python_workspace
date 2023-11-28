# 3. Accept 2 integers. print all nos which are mirror nos falling
# between the range.
# eg: first no 300
#  second no 400
# 303,313,323.......393
# try to incorporate error handling feature too in all the
# above problems.

try:
    # Accept 2 integers from the user
    first_no = int(input("Enter the first number: "))
    second_no = int(input("Enter the second number: "))

    # Check for each possible first and last digit
    for num in range(1, 10):  # Starting from 1 to exclude numbers like 030
        # Construct the mirror number for all middle digits from 0 to 9
        for middle in range(10):
            mirror_num = int(str(num) + str(middle) + str(num))

            # Check if the mirror number is within the range
            if first_no <= mirror_num <= second_no:
                print(mirror_num)

except ValueError:
    print("Please enter valid integers.")
