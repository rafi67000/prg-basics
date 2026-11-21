# Liczenie elementów większych od wartości podanej przez użytkownika
arr = [1.5, 3.2, 7.8, 2.1, 9.4, 5.0]
number = float(input("Enter value: "))

count = 0
for value in arr:
    if value > number:
        count += 1

print("Array:", arr)
print("Number of elements greater than", number, ":", count)
