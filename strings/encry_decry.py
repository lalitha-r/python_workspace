# 2. Input is an encrypted  string where there will be chars followed by number. The way to decrypt is
# to repeat the chars, by the number of times. Print the decrypted word and its length. If there are any special
# chars, all the chars between the number and special char are ignored.
#  eg - ac2bd3 means acacbdbdbd.
#  ac2acc#cd3 acaccdcdcd
import re
# get the input string from user
encrypt_string = input("enter the string to be decrypt :")
# using regex extracting the chars and numbers from input
matches = re.findall(r'([a-zA-Z]+)(\d+)', encrypt_string)
decrypt_string = ""
for match in matches:
    # it repeat the chars by the number of times
    decrypt_string += match[0] * int(match [1])

print(f"the decrypted string is :{decrypt_string}")
print(f"the length of the decrypted string is: {len(decrypt_string)}")

# output :
# enter the string to be decrypt :ac2acc#cd3
# the decrypted string is :acaccdcdcd
