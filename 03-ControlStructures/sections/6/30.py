#tworzenie kuponu Lotto z liczbami od 1 do 49

#pętla odpowiadająca za siedem wierszy
for i in range(1, 8):

    #pętla odpowiadająca za siedem kolumn
    for j in range(7):

        #obliczenie liczby do wyświetlenia
        number = i + j * 7 #j * 7 dodaje kolejne wielokrotności liczby 7

        print(number, end=' ')

    #przejście do następnego wiersza
    print()