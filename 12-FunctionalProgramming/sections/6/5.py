# Program wyswietla liczby podzielne przez 2 i 3.

numbers = list(range(1, 21)) # liczby od 1 do 20

filter_func = lambda x: x % 2 == 0 and x % 3 == 0

result = list(filter(filter_func, numbers)) # filtrowanie liczb

print(result) # wyswietlenie wynikow
