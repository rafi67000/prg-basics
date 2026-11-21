# Funkcja tworzy tablicę 2D wypełnioną zerami
def create_2d_arr(x, y):
    arr = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(0)
        arr.append(row)
    return arr

# Tworzenie tablicy 3x5
arr = create_2d_arr(3, 5)

for row in arr:
    for value in row:
        print(value, end=" ")
    print()
