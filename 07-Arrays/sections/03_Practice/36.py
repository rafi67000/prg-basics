# Transponowanie macierzy
def transpose_matrix(m):
    transposed = []
    for j in range(len(m[0])):
        row = []
        for i in range(len(m)):
            row.append(m[i][j])
        transposed.append(row)
    return transposed

def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]
matrix3 = [[5, 6, 7, 8]]

print("Transposed matrix 1:")
print_matrix(transpose_matrix(matrix1))
print("Transposed matrix 2:")
print_matrix(transpose_matrix(matrix2))
print("Transposed matrix 3:")
print_matrix(transpose_matrix(matrix3))
