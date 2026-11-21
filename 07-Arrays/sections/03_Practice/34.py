# Zamiana pierwszej i ostatniej kolumny w macierzy 3x5
arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Before:")
for row in arr:
    for value in row:
        print(value, end=" ")
    print()

# Zamiana wartości w pierwszej i ostatniej kolumnie każdego wiersza
for i in range(len(arr)):
    temp = arr[i][0]
    arr[i][0] = arr[i][len(arr[i]) - 1]
    arr[i][len(arr[i]) - 1] = temp

print("After:")
for row in arr:
    for value in row:
        print(value, end=" ")
    print()
