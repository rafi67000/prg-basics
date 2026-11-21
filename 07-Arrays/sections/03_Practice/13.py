# Wyświetlanie elementów, które występują tylko jeden raz
arr = [2, 3, 2, 5, 8, 1, 9, 8]

print("Array:", *arr)
print("Unique elements:", end=" ")
for value in arr:
    count = 0
    for other in arr:
        if value == other:
            count += 1
    if count == 1:
        print(value, end=" ")
print()
