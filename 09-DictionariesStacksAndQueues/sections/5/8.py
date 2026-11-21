# Słownik z cenami produktów
prices = {
    'milk': 1.49,
    'butter': 2.09,
    'juice': 1.19,
    'bread': 1.99
}

# Koszyk z ilością produktów
cart = {
    'juice': 3,
    'bread': 1,
    'milk': 2
}

# Obliczenie łącznej ceny zakupów
total = 0

for item in cart:
    total += prices[item] * cart[item]

# Wyświetlenie wyniku
print("Total cost:", round(total, 2))