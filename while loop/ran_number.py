import random

# Generate a random number between 3 and 9 (inclusive)
computerNo = random.randint(3, 9)

attempt = 0
while True:
    # Get user input for their guess
    userNo = int(input("Guess the number (between 3 and 9):"))
    
    # Check if the user's guess is too low, too high, or correct
    if userNo < computerNo:
        print("Low")
    elif userNo > computerNo:
        print("High")
    else:
        print("Congratulations! You guessed the number correctly.")
        break
    
    attempt += 1

print("User guessed the number in", attempt, "attempts.")