# 25. Sprawdzanie kodu produktu
def product_code_is_valid(product_code):
    # product_code – cztery cyfry zapisane jako tekst
    if len(product_code) != 4 or not product_code.isdigit():
        return False
    digit_sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    # digit_sum – suma trzech pierwszych cyfr
    control_digit = digit_sum % 7  # control_digit – oczekiwana czwarta cyfra
    return control_digit == int(product_code[3])

print(product_code_is_valid("1082"))
print(product_code_is_valid("2035"))
print(product_code_is_valid("1114"))
print(product_code_is_valid("7071"))
