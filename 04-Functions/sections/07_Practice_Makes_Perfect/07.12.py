# 12. Prosty kalkulator
def calculate(number1, number2, operator):
    # number1, number2 – liczby; operator – znak działania
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "%":
        return number1 % number2
    elif operator == "**":
        return number1 ** number2
    else:
        return "Unknown operator"

print(calculate(2, 3, "+"))
print(calculate(2, 3, "%"))
print(calculate(2, 3, "**"))
print(calculate(2, 3, "*"))
print(calculate(2, 3, "-"))
