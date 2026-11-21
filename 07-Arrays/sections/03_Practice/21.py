# Przeniesienie parzystych na początek listy, a potem nieparzystych
arr = [7, 9, 2, 4, 5, 6]
result = []

for value in arr:
    if value % 2 == 0:
        result.append(value)

for value in arr:
    if value % 2 != 0:
        result.append(value)

print("Array:", arr)
print("Changed array:", result)
