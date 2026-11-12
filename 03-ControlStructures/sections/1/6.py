#Sprawdza czy podana liczba jest parzysta czy nieparzysta

number = int(input('Enter number: '))  #pobranie liczby

#operator % zwraca resztę z dzielenia
if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')