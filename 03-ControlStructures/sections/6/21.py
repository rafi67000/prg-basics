#rozmienianie kwoty na jak najmniejszą liczbę monet

amount = int(input('Enter the amount in PLN: '))

#obliczenie liczby monet 5-złotowych
coins_5 = amount // 5
amount = amount % 5

#obliczenie liczby monet 2-złotowych
coins_2 = amount // 2
amount = amount % 2

#obliczenie liczby monet 1-złotowych
coins_1 = amount

#wyświetlenie wyniku
print(f'The amount of PLN is shown in coins:')
print(f'5 PLN coins: {coins_5}')
print(f'2 PLN coins: {coins_2}')
print(f'1 PLN coins: {coins_1}')