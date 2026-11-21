import queue

# Odwracanie tekstu za pomocą stosu
def reverse(text):
    stack = queue.LifoQueue()
    # Dodajemy kolejne znaki na stos
    for char in text:
        stack.put(char)

    result = ''
    # Odczytujemy znaki w odwrotnej kolejności
    while not stack.empty():
        result += stack.get()
    return result

# Pobranie i wyświetlenie tekstu
text = input('Text: ')
print(reverse(text))
