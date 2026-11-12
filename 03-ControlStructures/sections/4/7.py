#obliczanie sumy liczb parzystych od 1 do 10

total_sum = 0

#przechodzenie po liczbach od 1 do 10
for i in range(1, 11):

    #jeśli liczba jest nieparzysta pomija ją
    if i % 2 != 0:
        continue

    #dodanie liczby parzystej do sumy
    total_sum += i

print(f'Sum of even numbers in the range <1,10> is {total_sum}')