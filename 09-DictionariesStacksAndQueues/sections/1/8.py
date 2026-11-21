# Słownik z produktami i ich cenami
price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

# Wyświetlenie cen przed obniżką
print("Before discount:")

for item in price_list:
    print(item, price_list[item])

# Obliczenie sumy cen wszystkich produktów
print("Total:", sum(price_list.values()))

# Obniżenie cen o 10%
for item in price_list:
    price_list[item] = round(price_list[item] * 0.9, 2)

# Wyświetlenie cen po obniżce
print("\nAfter 10% discount:")

for item in price_list:
    print(item, price_list[item])

# Obliczenie sumy cen po obniżce
print("Total:", sum(price_list.values()))