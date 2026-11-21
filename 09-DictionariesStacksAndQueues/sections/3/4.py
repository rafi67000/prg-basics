import queue

# Pobranie liczby od użytkownika
number = int(input('Natural number: '))

# Tworzenie pustego stosu
stack = queue.LifoQueue()

# Obsługa liczby 0
if number == 0:
    stack.put(0)

# Dzielenie liczby przez 2 i zapisywanie reszt
while number > 0:
    stack.put(number % 2)
    number = number // 2

# Odczytanie liczb ze stosu
binary = ''

while not stack.empty():
    binary += str(stack.get())

# Wyświetlenie liczby binarnej
print('Binary number:', binary)