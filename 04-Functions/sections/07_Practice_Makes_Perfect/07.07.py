# 7. Suma cyfr parzystych albo nieparzystych
def digit_sum_by_type(number, even):
    # number – badana liczba; even – True dla parzystych, False dla nieparzystych
    total = 0  # total – suma wybranych cyfr
    for char in str(abs(number)):  # char – cyfra zamieniona na tekst
        digit = int(char)  # digit – cyfra jako liczba
        if even and digit % 2 == 0:
            total += digit
        elif not even and digit % 2 != 0:
            total += digit
    return total

print(digit_sum_by_type(3124, True))
print(digit_sum_by_type(3124, False))
print(digit_sum_by_type(20576, False))
print(digit_sum_by_type(20576, True))
print(digit_sum_by_type(13115, True))
