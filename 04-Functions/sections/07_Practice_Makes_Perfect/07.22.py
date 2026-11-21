# 22. Obliczanie wyrażenia z jednocyfrowymi liczbami i + oraz -
def expression_value(expression):
    # expression – tekst zawierający cyfry oraz znaki + i -
    total = 0  # total – wynik obliczeń
    current_number = 0  # current_number – aktualnie odczytana cyfra
    sign = 1  # sign – 1 dla dodawania, -1 dla odejmowania

    for char in expression:
        if char.isdigit():
            current_number = int(char)
            total += sign * current_number
        elif char == "+":
            sign = 1
        elif char == "-":
            sign = -1

    return total

print(expression_value("2+3"))
print(expression_value("3+8+1"))
print(expression_value("2+3-4+5-0"))
