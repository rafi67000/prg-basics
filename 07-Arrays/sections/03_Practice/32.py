# Znajdowanie minimum, maksimum oraz ich położenia w macierzy
arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

minimum = arr[0][0]
maximum = arr[0][0]
min_row = 0
min_col = 0
max_row = 0
max_col = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < minimum:
            minimum = arr[i][j]
            min_row = i
            min_col = j
        if arr[i][j] > maximum:
            maximum = arr[i][j]
            max_row = i
            max_col = j

print("Minimum:", minimum, "row:", min_row + 1, "column:", min_col + 1)
print("Maximum:", maximum, "row:", max_row + 1, "column:", max_col + 1)
