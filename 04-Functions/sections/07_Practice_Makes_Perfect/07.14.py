# 14. n-ta wartość ciągu Fibonacciego (pierwsza wartość ma numer 1)
def fibonacci(n):
    # n – numer wyrazu ciągu
    if n <= 0:
        return None
    previous = 0  # previous – poprzedni wyraz ciągu
    current = 1   # current – aktualny wyraz ciągu
    for i in range(1, n):  # i – numer kroku obliczeń
        previous, current = current, previous + current
    return previous

print(fibonacci(5))
print(fibonacci(9))
