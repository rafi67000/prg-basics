# Program przelicza kwoty z EUR na PLN.

transactions_in_eur = [15.90, 38.47, 4.07, 132.70, 9.15] # kwoty w euro

eur_to_pln = lambda m: m * 4.5 # funkcja przeliczajaca z EUR na PLN

transactions_in_pln = list(map(eur_to_pln, transactions_in_eur)) # przeliczenie na PLN

for amount in transactions_in_pln:
    print(f"{amount:.2f}") # wyswietlenie kwoty 2 cyfry po przecinku
