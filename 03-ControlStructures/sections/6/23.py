#tworzenie tabliczki mnożenia dla podanej liczby

number = int(input('Enter number: '))

#mnożenie podanej liczby przez liczby od 1 do 10
for i in range(1, 11):
    result = number * i
    print(f'{number} x {i} = {result}')