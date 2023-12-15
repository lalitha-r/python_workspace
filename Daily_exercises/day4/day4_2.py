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
global board


def game_board():  # function to generate the board
    rows = 6
    cols = 6

    board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append('*')

        board.append(row)

    return board


def print_board():
    for row in board:
        print(' '.join(row))
        print()


def roll_dice():  # roll dice to generate a random digit between 1 and 6
    return random.randint(1, 6)


def play_game():  # game logic
    # initialize the board and scores
    board = game_board()
    score_A = 0
    score_B = 0

    # Loop untill one of the player wins
    while True:

        # print the board with spacing
        # for row in board:
        #     print(' '.join(row))
        # print()
        print_board()

        print(f"current score-player A:{score_A}, player B:{score_B}")
        input("player A's turn: press enter to roll the dice twice")

        for i in range(2):
            row_A, col_A = roll_dice(), roll_dice()
            print(f"player A rolled: ({row_A}, {col_A})")

            if board[row_A - 1][col_A - 1] == 'B':
                score_A += 1
                board[row_A - 1][col_A - 1] = 'A'
            else:
                board[row_A - 1][col_A - 1] = 'A'

            if score_A >= 5:
                print_board(board)
                print("player A wins")
                return

        print_board(board)

        print(f"current score-player A:{score_A}, player B:{score_B}")
        input("player B's turn: press enter to roll the dice twice")
        for i in range(2):
            row_B, col_B = roll_dice(), roll_dice()
            print(f"player B rolled: ({row_B}, {col_B})")

            if board[row_B - 1][col_B - 1] == 'A':
                score_B += 1
                board[row_B - 1][col_B - 1] = 'B'
            else:
                board[row_B - 1][col_B - 1] = 'B'

            if score_B >= 5:
                print_board(board)
                print("player B wins")
                return
        print_board(board)


play_game()
