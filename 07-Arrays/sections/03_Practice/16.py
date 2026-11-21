# Wyświetlanie krotki w odwrotnej kolejności
values = (10, 20, 30, 40, 50)

print("Tuple:", end=" ")
for i in range(len(values)):
    print(values[i], end=",")
print()

print("Reverse order:", end=" ")
i = len(values) - 1
while i >= 0:
    print(values[i], end=",")
    i -= 1
print()
