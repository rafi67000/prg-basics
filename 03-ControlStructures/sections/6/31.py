#losowanie 20 liczb całkowitych od 5 do 10

import random  #import biblioteki do losowania

#pętla wykonuje się 20 razy
for i in range(20):

    #losowanie liczby od 5 do 10
    number = random.randint(5, 10)#random.randint(5, 10) losuje liczbę całkowitą od 5 do 10, włącznie z obiema granicami

    #wyświetlenie wylosowanej liczby
    print(number, end=' ')