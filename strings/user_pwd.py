import re

# Get the username and password from the user
username = input("Enter your username: ")
password = input("Enter your password: ")

# Define a regular expression pattern for the username
username_pattern = r'^.+@(com|edu|tech|org)$'

# Define a regular expression pattern for the password
password_pattern = r'^(.).(.).*(\1\3\2{3}\d{3})$'

# Check if the username and password match their respective patterns
if re.match(username_pattern, username) and re.match(password_pattern, password):
    print("Username and password are correct.")
else:
    print("Username and password do not match the specified criteria.")