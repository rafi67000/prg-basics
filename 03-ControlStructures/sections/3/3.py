#sprawdza czy osoba ma prawo do zniżki

age = int(input('Enter your age: '))

#zniżka dla osób poniżej 18 lat lub od 65 lat
if age < 18 or age >= 65:
    print('Discount available')
else:
    print('Discount not available')