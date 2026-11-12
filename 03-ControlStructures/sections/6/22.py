#wyświetlanie liczb od 1 do 30
#THREE dla liczb podzielnych przez 3
#FIVE dla liczb podzielnych przez 5
#BINGO dla liczb podzielnych przez 3 i 5

for i in range(1, 31):

    #liczba podzielna jednocześnie przez 3 i 5
    if i % 3 == 0 and i % 5 == 0:
        print('BINGO', end=' ')

    #liczba podzielna przez 3
    elif i % 3 == 0:
        print('THREE', end=' ')

    #liczba podzielna przez 5
    elif i % 5 == 0:
        print('FIVE', end=' ')

    #pozostałe liczby
    else:
        print(i, end=' ')