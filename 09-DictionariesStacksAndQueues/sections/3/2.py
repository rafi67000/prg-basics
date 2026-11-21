import queue

# Tworzenie stosu odwiedzonych stron
visited_websites = queue.LifoQueue()

# Dodawanie przykładowych stron
visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

# Aktualnie otwarta strona
current = None

while True:
    website = input('Enter website name (0 for back): ')

    # Powrót do poprzedniej strony
    if website == '0':
        if visited_websites.empty():
            break

        print('<-- Going back to a previously visited website')
        current = visited_websites.get()

    # Przejście na nową stronę
    elif website != '':
        if current is not None:
            visited_websites.put(current)

        current = website

    # Wyświetlenie aktualnej strony
    print('You are currently viewing:', current)
    print()