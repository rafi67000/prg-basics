# The binary numeral system is a positional numeral system that requires only two digits to write numbers: 0 and 1. The hexadecimal numeral system is a positional numeral system that uses sixteen distinct symbols, most often the symbols "0" to "9" to represent values 0 to 9, and "A" to "F" (or alternatively "a" to "f") to represent values from ten to fifteen. Both are widely used in mathematics, computer science and digital electronics. Write a program that reads an integer number from the keyboard and prints that value as a binary and hexadecimal number. To convert a decimal number to binary or hexadecimal value, use the available Python functions. Sample result:

decimal = int(input('Enter decimal value: '))
binary = bin(decimal)
hexadecimal = hex(decimal)

print(f"""
Decimal value: {decimal}
Binary value: {binary}
Hexadecimal value: {hexadecimal}
""")