num = int(input("Enter a number: "))


    # Continue until n becomes 1
    while num != 1:
        print(n, end=", ")
        
        # Check if n is even
        if num % 2 == 0:
            num = num // 2  # Divide by 2
        else:
            num = 3*num + 1  # Multiply by 3 and add 1

    # Print the last number in the sequence
    print(num)