#obliczanie kwoty do zapłaty za produkty

number_of_products = int(input('Number of products purchased: '))
product_price = float(input('Product price: '))

#oblicza wartość wszystkich produktów
total_price = number_of_products * product_price

#rabat naliczany za produkty powyżej dwóch sztuk
if number_of_products > 2:
    discount = (number_of_products - 2) * product_price * 0.25
else:
    discount = 0

#obliczenie końcowej kwoty
amount_to_pay = total_price - discount

print(f'Amount to pay: {amount_to_pay:.2f}')