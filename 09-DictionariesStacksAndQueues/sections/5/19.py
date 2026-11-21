import json

# Wczytanie rezerwacji
def load_reservations():
    with open('reservations.json', encoding='utf-8') as file:
        return json.load(file)['reservations']

# Obliczenie wartości rezerwacji
def reservation_value(reservation):
    # Koszt to liczba nocy razy cena za noc
    return reservation['nights'] * reservation['price_per_night']

# Podsumowanie rezerwacji
def show_summary(reservations):
    paid_count = 0
    unpaid_count = 0
    paid_total = 0
    unpaid_total = 0

    for reservation in reservations:
        value = reservation_value(reservation)
        # Osobno liczymy rezerwacje opłacone i nieopłacone
        if reservation['paid']:
            paid_count += 1
            paid_total += value
        else:
            unpaid_count += 1
            unpaid_total += value

    print('Number of rooms:', len(reservations))
    print('Paid reservations:', paid_count)
    print('Unpaid reservations:', unpaid_count)
    print('Total value of paid reservations:', round(paid_total, 2))
    print('Total value of unpaid reservations:', round(unpaid_total, 2))

# Uruchomienie podsumowania
reservations = load_reservations()
show_summary(reservations)
