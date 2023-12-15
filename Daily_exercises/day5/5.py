def initialize_theater(rows, seats_per_row):
    seating = {chr(65 + i): [False] * seats_per_row for i in range(rows)}
    available_seats = rows * seats_per_row
    return seating, available_seats


output = initialize_theater(5, 10)
print(output)
