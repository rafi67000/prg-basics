# 18. n-ta liczba pierwsza (numerowanie od 1)
def nth_prime(n):
    # n – pozycja szukanej liczby pierwszej
    found = 0  # found – ile liczb pierwszych już znaleziono
    candidate = 1  # candidate – aktualnie sprawdzana liczba

    while found < n:
        candidate += 1
        is_prime = True  # is_prime – informacja, czy liczba jest pierwsza

        for divisor in range(2, candidate):
            if candidate % divisor == 0:
                is_prime = False
                break

        if is_prime:
            found += 1

    return candidate

print(nth_prime(1))
print(nth_prime(5))
