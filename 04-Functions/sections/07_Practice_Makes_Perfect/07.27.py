# 27. Silnia obliczana rekurencyjnie
def factorial(n):
    # n – liczba naturalna, dla której obliczamy silnię
    if n == 0 or n == 1:
        return 1  # Warunek stopu rekurencji
    return n * factorial(n - 1)  # Wywołanie funkcji dla mniejszej liczby

print("5! =", factorial(5))
