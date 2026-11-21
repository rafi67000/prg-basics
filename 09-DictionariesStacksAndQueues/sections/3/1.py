import queue

# Tworzenie pustego stosu
stack = queue.LifoQueue()

# Dodawanie liczb na stos
for number in (2, 3, 7, 4, 1, 9, 8):
    stack.put(number)

# Zdjęcie dwóch ostatnich liczb ze stosu i ich zsumowanie
sum1 = stack.get() + stack.get()
print("Sum of the last two numbers:", sum1)

# Sumowanie pozostałych elementów stosu
sum2 = 0

while not stack.empty():
    sum2 += stack.get()

print("Sum of the remaining elements:", sum2)