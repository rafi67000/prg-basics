# Sortowanie bąbelkowe
def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array

array1 = [8, 3, 1, 9, 4]
array2 = [15, -2, 7, 0, 21]
array3 = [5, 5, 2, 10, 1]

print("Array 1 sorted:", bubblesort(array1))
print("Array 2 sorted:", bubblesort(array2))
print("Array 3 sorted:", bubblesort(array3))
