import queue

# Tworzenie kolejki plików do wydruku
files_to_print = queue.Queue()

while True:
    # Wyświetlenie menu
    print('1. Add file to print')
    print('2. Print file')
    print('0. Quit')

    menu = input('Select an option: ')

    # Dodawanie pliku do kolejki
    if menu == '1':
        file_name = input('Enter file name to print: ')
        files_to_print.put(file_name)

    # Drukowanie pierwszego pliku z kolejki
    elif menu == '2':
        if not files_to_print.empty():
            file_name = files_to_print.get()
            print('File', file_name, 'is currently being printed. Please wait!')
        else:
            print('There are no files to print.')

    # Zakończenie programu
    elif menu == '0':
        break

    # Obsługa nieprawidłowej opcji
    else:
        print('Unknown option.')

    print()