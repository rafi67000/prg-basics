# Zamiana elementów głównej przekątnej na 1
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(matrix)):
    matrix[i][i] = 1

# Wyświetlanie macierzy
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
