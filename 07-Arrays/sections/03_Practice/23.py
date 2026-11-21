# Zwracanie losowego elementu listy
import random

def rand_elem(array):
    index = random.randint(0, len(array) - 1)
    return array[index]

arr = ["apple", "banana", "orange", "pear", "plum"]

# Kilka losowych elementów
for i in range(5):
    print(rand_elem(arr))
