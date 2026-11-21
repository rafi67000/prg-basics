# Sprawdzanie, czy pierwsza lista jest podzbiorem drugiej
array1 = [2, 5]
array2 = [1, 2, 3, 4, 5, 6]

is_subset = True
for value in array1:
    if value not in array2:
        is_subset = False

print("Array1:", array1)
print("Array2:", array2)
print("Is subset:", is_subset)
