# Problem #1
# write a program that reads a passage and reverses the order of
# letters in each word while keeping the word order intact. Use function.
# Eg- input - I am Sayur
# Output I ma ruyaS
def reverse_order(passage):

    words = passage.split()
    reverse_passage = ""
    for word in words:
        reverse_word = word[::-1]
        reverse_passage += reverse_word + " "
    return reverse_passage.strip()


input_passage = input("enter the passage:")
output_passage = reverse_order(input_passage)
print(f"the reversed passage is {output_passage}")


def add_comma(passage):
    words = passage.split()
    output = ""
    for word in words:
        output += word + ',' + " "

    return output.strip()
