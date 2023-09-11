#Get an input string from the user. Add a space at every 3rd char.
#eg input = abcdefg , output = ab cd ef g

inputString = "pythonstring" 
i = 0 #counter to track the chars
newString = ""
while i < len(inputString): 
    newString += inputString[i : i+2]# add characters from i to i+2
    if i + 2 < len(inputString) : 
        newString += " " #add space
    i+=2 # incrementing i as we need to print two letters followed by space

print (newString)


#output
py th on st ri ng