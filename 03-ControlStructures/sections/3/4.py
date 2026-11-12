#sprawdza czy przynajmniej jedna liczba nie jest ujemna

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

#sprawdza czy przynajmniej jedna liczba jest większa lub równa zero
if not x < 0 or not y < 0:
    print(f'At least one of the numbers {x} and {y} is not negative')
else:
    print('Both numbers are negative')