# slownik
stock = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}

# Lista produktów: nazwa wyrównana do lewej (22 znaki), ilość do prawej (5 znaków)
for product, quantity in stock.items():
    print(f"{product:<22}{quantity:>5}")

# values() zwraca same wartości (ilości), sum() je sumuje.
print(f"Total number of products: {sum(stock.values())}")
