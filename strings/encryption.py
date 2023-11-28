encrypted_str = input("Enter the encrypted string: ")# ac2bd3  #acacbdbdbd
decrypted = []

i = 0
while i < len(encrypted_str):#5
    char = encrypted_str[i] #char=a

    # Check if the character is a digit
    if char.isdigit():
        repeat_count = ""
        prev_chars = []  # Initialize a list to store characters before the digit

        # Extract the entire sequence of digits
        while i < len(encrypted_str) and encrypted_str[i].isdigit():
            repeat_count += encrypted_str[i]
            i += 1

        # Find the characters before the number
        while i < len(encrypted_str) and not encrypted_str[i].isdigit():
            prev_chars.append(encrypted_str[i])
            i += 1

        # Repeat the previous characters as a group and append to the decrypted list
        decrypted.extend(prev_chars * int(repeat_count))
    else:
        # Append the character to the decrypted list
        decrypted.append(char)
        i += 1

decrypted_string = "".join(decrypted)
print(f"Decrypted String: {decrypted_string}")
print(f"Length of Decrypted String: {len(decrypted_string)}")



      


        
       
  




      


