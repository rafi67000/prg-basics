#wyświetlanie pierwszych 20 liczb ciągu Fibonacciego

a = 0  #pierwsza liczba ciągu
b = 1  #druga liczba ciągu

#pętla wykonuje się 20 razy
for i in range(20):

    #wyświetlenie aktualnej liczby
    print(a, end=' ')

    #obliczenie kolejnej liczby
    next_number = a + b

    #przesunięcie wartości
    a = b
    b = next_number