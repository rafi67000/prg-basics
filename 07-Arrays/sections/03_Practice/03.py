# Wyświetlanie listy w odwrotnej kolejności
arr = [15, 8, 31, 47, 2, 19]

print("existed array:", end=" ")
for value in arr:
    print(value, end=" ")
print()

print("reverse array:", end=" ")
i = len(arr) - 1
while i >= 0:
    print(arr[i], end=" ")
    i -= 1
print()
