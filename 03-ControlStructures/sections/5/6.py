#obliczanie sumy liczb parzystych od 1 do N

N = 10
sum_even = 0  #suma liczb parzystych
i = 1  #początkowa liczba

#pętla działa dopóki i nie przekroczy N
while i <= N:

    #sprawdza czy liczba jest parzysta
    if i % 2 == 0:
        sum_even += i

    #przejście do kolejnej liczby
    i += 1

print(f'The sum of even numbers from 1 to {N} is: {sum_even}')