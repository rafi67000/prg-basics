# 5. Sprawdzanie, czy tekst jest liczbą binarną
def is_binary(binary_number):
    # binary_number – tekst, który może zawierać tylko 0 i 1
    for digit in binary_number:  # digit – kolejny znak
        if digit != "0" and digit != "1":
            return False
    return len(binary_number) > 0  # Pusty tekst nie jest liczbą binarną

print(is_binary("101101"))
print(is_binary("1311a10100"))
