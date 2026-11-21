# Zadanie 7.29 – potęgowanie rekurencyjne

# 2. Potęgowanie rekurencyjne
def power(x, n):
    # x – podstawa potęgi; n – wykładnik nieujemny
    if n == 0:
        return 1  # Każda niezerowa liczba do potęgi 0 daje 1
    return x * power(x, n - 1)  # Mnożymy x przez mniejszą potęgę

result = power(5, 3)  # result – wartość 5 do potęgi 3
print("5^3 =", result)
