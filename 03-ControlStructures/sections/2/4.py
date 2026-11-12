#kalkulator robi podstawowe działania

number1 = float(input('Enter first number: '))  # Pierwsza liczba
number2 = float(input('Enter second number: '))  # Druga liczba
operator = input('Enter operator (+, -, *, /): ')  # Działanie

#wybór odpowiedniego działania
if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2
else:
    result = 'Incorrect operator'

#wynik
print(f'{number1} {operator} {number2} = {result}')