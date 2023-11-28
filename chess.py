board_size = 8 # initialize the size of board as 8

# Loop through rows
for row in range(board_size):
    # Loop through columns
    for col in range(board_size):
        # Check if the sum of the row and column indices is even
        if (row + col) % 2 == 0:
            # Print a white square
            print('\u25A1', end=' ')
        else:
            # Print a black square
            print('\u25A0', end=' ')
    # Move to the next line for the next row
    print()