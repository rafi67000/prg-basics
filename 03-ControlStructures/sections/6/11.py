#analiza obniżki ceny produktu

current_price = 140.00  #aktualna cena 
previous_price = 200.00  #poprzednia cena

#obliczenie procentowej obniżki
price_reduction = (previous_price - current_price) / previous_price * 100

print(f'Current product price: {current_price:.2f}')
print(f'Previous product price: {previous_price:.2f}')

# :.2f wyświetla dwie cyfry po przecinku a :.0f zaokrągla wynik procentowy do liczby całkowitej.
#sprawdzenie czy obniżka wynosi co najmniej 10%
if price_reduction >= 10:
    print('Buy the product!!')
    print(f'Product price reduced by {price_reduction:.0f}%')