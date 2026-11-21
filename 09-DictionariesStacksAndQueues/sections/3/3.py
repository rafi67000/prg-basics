import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"
expression2 = "[(2+3]/4)"
expression3 = "(2-3*4+(5/6)"

# Funkcja sprawdzająca poprawność nawiasów
def brackets_ok(expression):
    stack = queue.LifoQueue() # Last In First Out

    for char in expression:
        # Dodawanie nawiasów otwierających na stos
        if char in "([{":
            stack.put(char)

        # Sprawdzanie nawiasów zamykających
        elif char in ")]}":
            if stack.empty():
                return False

            opening = stack.get()

            if char == ")" and opening != "(":
                return False
            if char == "]" and opening != "[":
                return False
            if char == "}" and opening != "{":
                return False

    # Sprawdzenie czy stos jest pusty
    return stack.empty()


# Sprawdzenie podanych wyrażeń
for expression in (expression1, expression2, expression3):
    if brackets_ok(expression):
        print(expression, "-> brackets OK")
    else:
        print(expression, "-> brackets NOT correct")