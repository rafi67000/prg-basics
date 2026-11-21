# Zliczanie wystąpień wartości w krotce
values = (50, 20, 40, 50, 30, 50)
number = 50

count = 0
for value in values:
    if value == number:
        count += 1

print("Tuple:", end=" ")
for value in values:
    print(value, end=",")
print()
print("Value:", number)
print("Number of occurrences:", count)
