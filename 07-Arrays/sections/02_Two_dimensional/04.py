# Plan miejsc w kinie: A = dostępne, B = zajęte
cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
]

# Liczba wszystkich miejsc
def seats_total(seats):
    total = 0
    for row in seats:
        total += len(row)
    return total

# Liczba dostępnych miejsc
def seats_available(seats):
    available = 0
    for row in seats:
        for seat in row:
            if seat == "A":
                available += 1
    return available

# Liczba zajętych miejsc
def seats_booked(seats):
    booked = 0
    for row in seats:
        for seat in row:
            if seat == "B":
                booked += 1
    return booked

# Status miejsca (numery w argumentach liczone od 1)
def seat_status(seats, row, place):
    if seats[row - 1][place - 1] == "A":
        return "available"
    else:
        return "booked"

print("CINEMA INFORMATION TABLE")
print("Total seats:", seats_total(cinema_seats))
print("Seats available:", seats_available(cinema_seats))
print("Seats booked:", seats_booked(cinema_seats))
print("Seat in row 1, place 1:", seat_status(cinema_seats, 1, 1))
print("Seat in row 5, place 5:", seat_status(cinema_seats, 5, 5))
print("Seat in row 3, place 5:", seat_status(cinema_seats, 3, 5))
