# Problem #1
# Wrote a program for seat reservation in a theatre.
# You can decide on the configuaration of the seats (no of rows and no of seats in each row, and a passage in between)
# When the user asks for tickets, you need to provide them tickets in the form of seat no.
# For eg, User ask for 3 seats in the middle. Output is F11, F12 , F13
# Print the theatre configuaration at the end of each transaction.

# Problem #2
# Same problem as above. Also calculate tickets price.
# Firsrt 3 rows - Rs100
# Rows 4 to 12 - Rs 200
# Rows 13 till top - Rs 300.
# 3 seats close to the wall on both sides costs less than the other seats in the same row.


# Class to represent a seat in the theatre

class Seat:
    def __init__(self, row, seat_number):
        self.row = row  # row name where the seat is in. eg: A
        # exact seat number  eg A1 denontes 1st seat in row A
        self.seat_number = seat_number
        self.is_reserved = False  # flag to denote if the seat is reserved or not

    # method to mark the seat as reserved
    def reserve(self):
        self.is_reserved = True

    # A custom string representation of an object to
    # represent the Seat object as custom string format
    # eg: seat = Seat('A', 1) and print(seat) will output 'A1' by implicitly calling __str__
    def __str__(self):
        return f'{self.row}{self.seat_number}'


class Theater:
    def __init__(self, rows, seats_per_row):
        print("")

    # @TODO show the seating arrangement in this format
    # Row A: E E E E E E E E E E
    # Row B: E E E E E E E E E E
    # Row C: E E E E E E E E E E
    # Row D: E E E E E E E E E E
    # Row E: E E E E E E E E E E
    def show_seating(self):
        print("")

    # after user enters the number of tickets.
    # @TODO write logic to reserve tickets
    # mark each ticket as X when reserved and update is_reserved as True
    def reserve_tickets(self, num_tickets):
        print("")


def main():
    print("")


if __name__ == "__main__":
    main()
