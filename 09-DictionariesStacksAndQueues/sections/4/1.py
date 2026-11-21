import queue

# Tworzenie pustej kolejki
people = queue.Queue()

# Dodawanie osób do kolejki
people.put('Michael')
people.put('Charlotte')
people.put('Olivia')

# Wyświetlenie liczby osób w kolejce
print('Number of queue elements:', people.qsize())

# Pobieranie osób z kolejki
while not people.empty():
    print(people.get())