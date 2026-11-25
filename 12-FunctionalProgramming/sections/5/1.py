# Program oblicza sume liczb za pomoca reduce.

from functools import reduce # import funkcji reduce

numbers = [1, 2, 3, 4, 5] # lista liczb

sum_func = lambda x, y: x + y

result = reduce(sum_func, numbers) # dodawanie liczb (zwraca jedną liczbe)

print(result) # wyswietlenie sumy
