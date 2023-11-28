import re
password = "abc"
if re.match("^[a-zA-Z]+$",password):
    print("Weak password-only alphabets")