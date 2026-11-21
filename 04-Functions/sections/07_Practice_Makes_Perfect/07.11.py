# 11. Tekst z liczb od 1 do n
def numbers_string(n):
    # n – ostatnia liczba do zapisania
    result = ""  # result – sklejany tekst z liczbami
    for number in range(1, n + 1):
        result += str(number)
    return result

print(numbers_string(11))
print(numbers_string(4))
