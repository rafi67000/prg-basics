# 4. Ukrywanie numeru karty
def hide(card_number):
    # card_number – numer karty zapisany jako tekst
    first = card_number[:2]  # first – pierwsze dwie cyfry
    last = card_number[-4:]  # last – ostatnie cztery cyfry
    stars = "*" * (len(card_number) - 6)  # stars – maska pozostałych cyfr
    return first + stars + last

print(hide("5290312400019022"))
