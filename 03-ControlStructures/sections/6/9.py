#sprawdza czy imię kończy się literą a

name = input('Enter name: ')

# Sprawdzenie ostatniego znaku imienia
if name.endswith('a'):
    print(f'{name} -- Polish female name')