import queue

# Stos do obliczeń RPN
stack = queue.LifoQueue()
print('Enter numbers, operators (+ - * /) or =')

while True:
    token = input('> ').strip()

    # Wyświetlenie wyniku i wyczyszczenie stosu
    if token == '=':
        if stack.qsize() == 1:
            print('Result:', stack.get())
        else:
            print('Incorrect expression')
        stack = queue.LifoQueue()

    # Wykonanie działania na dwóch liczbach
    elif token in ('+', '-', '*', '/'):
        if stack.qsize() < 2:
            print('Not enough numbers')
            stack = queue.LifoQueue()
            continue
        # Najpierw pobieramy drugi argument działania
        b = stack.get()
        a = stack.get()
        if token == '+':
            result = a + b
        elif token == '-':
            result = a - b
        elif token == '*':
            result = a * b
        else:
            if b == 0:
                print('Cannot divide by zero')
                stack = queue.LifoQueue()
                continue
            result = a / b
        # Wynik wraca na stos i może być użyty dalej
        stack.put(result)

    # Dodanie liczby na stos
    else:
        try:
            # Wpisaną liczbę zamieniamy na float
            stack.put(float(token))
        except ValueError:
            print('Enter a number or operator')
