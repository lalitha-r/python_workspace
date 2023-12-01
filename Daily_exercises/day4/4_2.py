# Problem #2
# You have 6 x 6 game board where each cell is shown as a *
# This is a two player dice game. The die has numbers 1 to 6.
# Each player rolls the dice twice. First roll is row number, second roll is col number.
# After the player rolls the dice, in the (row, col) enter the player's initial.
# If the player A rolls the dice and if  player B already has their initial in the same row,col
# add a point to A and change the initial to A.

# Player who gets 5 points first wins the game.
# Print the board each time after the user rolls and also print the current score.
# Use functions

import random


def game_board():
    rows = 6
    cols = 6

    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append('*')

        board.append(row)

    return board


def print_board(board):
    for row in board:
        print(' '.join(row))
        print()


def roll_dice():
    return random.randint(0, 5)  # Modified to generate 0-5 for indexing


def play_game(player_name):
    input(f"press enter  for {player_name} to roll ")

    # Roll the dice twice
    for i in range(2):
        row = roll_dice()
        col = roll_dice()
        print(f"{player_name} rolls: ({row}, {col})")

        if board[row][col] == '*':
            board[row][col] = player_name
        elif board[row][col] == player_name:
            # Player already has their initial here, add a point
            scores[player_name] += 1
        else:
            # Player B already has their initial here, add a point to A and change the initial to A
            scores[player_name] += 1
            board[row][col] = player_name

        # Print the current game board
        print_board(board)

        # Print the current scores
        print(f"Scores: Player A - {scores['A']}, Player B - {scores['B']}")


# Create a game board
board = game_board()

#  Initialize scores for players A and B
scores = {'A': 0, 'B': 0}

# Main game loop
while True:
    # Player A's turn
    print("Player A's turn:")
    play_game('A')

    # Check if Player A has reached 5 points and declare a winner
    if scores['A'] == 5:
        print("Player A wins!")
        break

    # Player B's turn
    print("Player B's turn:")
    play_game('B')

    # Check if Player B has reached 5 points and declare a winner
    if scores['B'] == 5:
        print("Player B wins!")
        break
