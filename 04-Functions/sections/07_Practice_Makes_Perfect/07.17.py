# 17. Suma cyfr, które występują więcej niż jeden raz
def repeated_digits_sum(number):
    # number – badana liczba
    digits = str(abs(number))  # digits – cyfry zapisane jako tekst
    total = 0  # total – suma wszystkich wystąpień powtarzających się cyfr
    for digit in digits:
        if digits.count(digit) > 1:
            total += int(digit)
    return total

print(repeated_digits_sum(1027))
print(repeated_digits_sum(230335))
print(repeated_digits_sum(513553007))
