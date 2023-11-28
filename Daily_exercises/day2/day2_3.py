# Problem #3
# Its is a single player game where the user starts with 0 points. User keeps rolling the
# dice.If the rolled number is 0, game ends. If the rolled number is even, then 2 points are
#  added. If the number is odd, then if the number is 1,3 then the user has to jump.
#  If the number is 5, then 3 points are added. The game ends when the user has 50 points.

import random

# Initialize variables
points = 0
game_over = False


while not game_over:
    # Roll the dice (random number between 1 and 6)
    roll = random.randint(1, 6)

    # Check the conditions
    if roll == 0:  # Game ends if rolled number is 0
        game_over = True
    elif roll % 2 == 0:  # If the number is even, add 2 points
        points += 2
    else:  # If the number is odd
        if roll in [1, 3]:  # Jump if the number is 1 or 3
            print("Jump!")
        elif roll == 5:  # Add 3 points if the number is 5
            points += 3

    # Print the rolled number and current points
    print(f"Rolled: {roll}, Points: {points}")

    # Check if the user has reached 50 points
    if points >= 50:
        game_over = True
        print("Congratulations! You've reached 50 points!")

# overall points
print(f"Game Over. You scored {points} points.")

# output:

# Rolled: 6, Points: 2
# Rolled: 2, Points: 4
# Rolled: 6, Points: 6
# Rolled: 5, Points: 9
# Rolled: 4, Points: 11
# Rolled: 2, Points: 13
# Jump!
# Rolled: 1, Points: 13
# Rolled: 6, Points: 15
# Rolled: 4, Points: 17
# Rolled: 6, Points: 19
# Rolled: 5, Points: 22
# Jump!
# Rolled: 1, Points: 22
# Jump!
# Rolled: 1, Points: 22
# Rolled: 6, Points: 24
# Rolled: 2, Points: 26
# Rolled: 6, Points: 28
# Rolled: 6, Points: 30
# Rolled: 4, Points: 32
# Jump!
# Rolled: 1, Points: 32
# Rolled: 4, Points: 34
# Rolled: 4, Points: 36
# Jump!
# Rolled: 3, Points: 36
# Rolled: 5, Points: 39
# Rolled: 2, Points: 41
# Rolled: 6, Points: 43
# Jump!
# Rolled: 3, Points: 43
# Rolled: 5, Points: 46
# Rolled: 4, Points: 48
# Jump!
# Rolled: 3, Points: 48
# Jump!
# Rolled: 3, Points: 48
# Rolled: 2, Points: 50
# Congratulations! You've reached 50 points!
# Game Over. You scored 50 points.
