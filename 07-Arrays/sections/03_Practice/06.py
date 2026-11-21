# Obliczanie średniej przy użyciu for
arr = [15, 8, 31, 47, 2, 19]

total = 0
for value in arr:
    total += value

average = total / len(arr)
print("Array:", arr)
print("Average:", average)
