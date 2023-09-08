i=1 # initializing the variable as 1
while i <= 10: #loop to continue for max of 10 lines
    line = '$' * i # Create a line with the appropriate number of '$' characters
    print(line.center(10)) # center align the line within a width of 10 characters

    user_input = input("Press Space to continue, any other key to stop: ") #get input from the user 

    if user_input == ' ': # if the input is space then print $
        i = i + 1 # increment i to print the next line of the diamond
    else:
        break # Exit the loop if the user enter different key

i = 9 # initializing the variable as 9 to print the diamond reverse
while i >= 1:
    line = '$' * i  # Create a line with the appropriate number of '$' characters
    print(line.center(10))  # Center align the line within a width of 10 characters

    user_input = input("Press Space to continue, any other key to stop: ")

    if user_input == ' ':
        i = i - 1  # Decrement i to print the next line of the diamond
    else:
        break  # Exit the loop if the user enter different key
 
   
# output

 
#     $     
# Press Space to continue, any other key to stop:   
#     $     
# Press Space to continue, any other key to stop:  
#     $$    
# Press Space to continue, any other key to stop:  
#    $$$    
# Press Space to continue, any other key to stop:  
#    $$$$   
# Press Space to continue, any other key to stop:  
#   $$$$$   
# Press Space to continue, any other key to stop:  
#   $$$$$$  
# Press Space to continue, any other key to stop:  
#  $$$$$$$  
# Press Space to continue, any other key to stop:  
#  $$$$$$$$ 
# Press Space to continue, any other key to stop:  
# $$$$$$$$$ 
# Press Space to continue, any other key to stop:  
# $$$$$$$$$$
# Press Space to continue, any other key to stop:  
# $$$$$$$$$ 
# Press Space to continue, any other key to stop:  
#  $$$$$$$$ 
# Press Space to continue, any other key to stop:  
#  $$$$$$$  
# Press Space to continue, any other key to stop:  
#   $$$$$$  
# Press Space to continue, any other key to stop:  
#   $$$$$   
# Press Space to continue, any other key to stop:  
#    $$$$   
# Press Space to continue, any other key to stop:  
#    $$$    
# Press Space to continue, any other key to stop:  
#     $$    
# Press Space to continue, any other key to stop:  
#     $     
# Press Space to continue, any other key to stop: ^[[1;2B^[[1;2D