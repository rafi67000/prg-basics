# Elementy pierwszej listy, których nie ma w drugiej
array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

for value in array1:
    if value not in array2:
        print(value, end=" ")
print()
