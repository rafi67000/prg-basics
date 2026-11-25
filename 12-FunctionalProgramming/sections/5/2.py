# Program oblicza sume liczb parzystych.

from functools import reduce # import funkcji reduce

numbers = [2, 4, 6, 3, 7, 5] # lista liczb

modulo_filter = lambda x: x % 2 == 0

even = list(filter(modulo_filter, numbers)) # wybor liczb parzystych

sum_func = lambda x, y: x + y

result = reduce(sum_func, even, 0) # dodawanie liczb parzystych

print(result) # wyswietlenie sumy
