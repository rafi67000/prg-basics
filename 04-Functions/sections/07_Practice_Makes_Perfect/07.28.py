# Zadanie 7.28 – suma liczb naturalnych rekurencyjnie

# 1. Suma liczb naturalnych od 1 do n
def sum_natural(n):
    # n – ostatnia liczba w sumowanym zakresie
    if n <= 0:
        return 0  # Warunek stopu rekurencji
    return n + sum_natural(n - 1)  # n dodane do sumy liczb mniejszych

result = sum_natural(10)  # result – suma liczb od 1 do 10
print("Sum from 1 to 10:", result)
