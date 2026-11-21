import queue

# Kolejka klientów i numer kolejnego biletu
customers = queue.Queue()
next_ticket = 1

while True:
    print('1. New customer (take a ticket)')
    print('2. Serve next customer')
    print('0. Quit')
    menu = input('Select an option: ')

    # Dodawanie klienta do kolejki
    if menu == '1':
        customers.put(next_ticket)
        print('Your ticket number:', next_ticket)
        print('Customers waiting:', customers.qsize())
        # Kolejny klient dostanie wyższy numer
        next_ticket += 1

    # Obsługa pierwszego klienta
    elif menu == '2':
        if customers.empty():
            print('No customers waiting.')
        else:
            # Pobieramy klienta, który czeka najdłużej
            print('Now serving ticket number', customers.get())

    elif menu == '0':
        break
    else:
        print('Unknown option.')
    print()
