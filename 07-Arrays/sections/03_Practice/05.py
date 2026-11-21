# Znajdowanie minimum i maksimum bez min() i max()
arr = [-15, 8, -31, 47, -2, 19]

minimum = arr[0]
maximum = arr[0]

for value in arr:
    if value < minimum:
        minimum = value
    if value > maximum:
        maximum = value

print("Array:", arr)
print("Minimum:", minimum)
print("Maximum:", maximum)
