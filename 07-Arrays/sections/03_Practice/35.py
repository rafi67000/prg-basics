# Tworzenie i wyświetlanie macierzy jednostkowej
def identity_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

# Funkcja wyświetlająca macierz
def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()

print("Identity matrix 3:")
print_matrix(identity_matrix(3))
print("Identity matrix 5:")
print_matrix(identity_matrix(5))
print("Identity matrix 8:")
print_matrix(identity_matrix(8))
