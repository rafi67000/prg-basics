# Program oblicza laczna wartosc produktow w magazynie.

stock = [(20, 5.50), (15, 8.30), (37, 3.85), (4, 11.60)] # ilosc i cena

price = lambda x: x[0] * x[1] # funkcja obliczajaca wartosc produktu

values = list(map(price, stock)) # wartosci produktow
total = sum(values) # suma wartosci

print(f"Products in stock: {stock}")
print(f"Total value: {total:.2f}")
