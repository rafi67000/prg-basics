# Program podnosi liczby do trzeciej potegi.

numbers = list(range(1, 21)) # liczby od 1 do 20
power_func = lambda x: x ** 3
result = list(map(power_func, numbers)) # trzecia potega

print(result) # wyswietlenie wynikow
