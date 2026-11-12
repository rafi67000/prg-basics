#wyszukiwanie N pierwszych liczb pierwszych

N = int(input('Enter the number of prime numbers: '))

counter = 0  #licznik znalezionych liczb pierwszych
number = 2  #pierwsza liczba od której zaczynamy

print('Prime numbers:', end=' ')

#szukanie liczb do momentu znalezienia N liczb pierwszych
while counter < N:

    is_prime = True  #początkowo zakładamy że liczba jest pierwsza

    #sprawdza czy liczba ma dzielniki inne niż 1 i sama siebie
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    #jeżeli liczba jest pierwsza, wyświetlamy ją
    if is_prime:
        print(number, end=' ')
        counter += 1

    #przejście do kolejnej liczby
    number += 1