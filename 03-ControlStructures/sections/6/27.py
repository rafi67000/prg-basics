#wyświetlanie klawiatury numerycznej za pomocą pętli while

i = 6

#pierwsza pętla odpowiada za kolejne wiersze
while i >= 0: #while i >= 0 wykonuje trzy wiersze

    j = 1

    #druga pętla odpowiada za liczby w jednym wierszu
    while j <= 3:
        print(f'{i+j}', end=' ') #while j <= 3 wyświetla trzy liczby w każdym wierszu
        j += 1

    #przejście do następnego wiersza
    print()

    #zmniejszenie wartości i o 3
    i -= 3