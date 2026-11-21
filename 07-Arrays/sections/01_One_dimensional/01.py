# Wyświetlanie podstawowych informacji o liście
arr = [2, 3, 7, 5, 4]

print("Array:", arr)
print("Number of elements:", len(arr))
print("First value:", arr[0])
print("Second value:", arr[1])
print("Last value:", arr[len(arr) - 1])
print("Last but one value:", arr[len(arr) - 2])
print("Sum of first and last value:", arr[0] + arr[len(arr) - 1])
print("Middle value:", arr[len(arr) // 2])

# Wyświetlanie elementów oddzielonych pojedynczą spacją
for value in arr:
    print(value, end=" ")
print()
