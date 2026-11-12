#obliczanie sumy liczb całkowitych od 5 do 10

total_sum = 0  #zmienna przechowująca sumę

# Pętla przechodzi przez liczby od 5 do 10
for i in range(5, 11):
    total_sum += i  # Dodanie aktualnej liczby do sumy

print(f'Sum is {total_sum}')