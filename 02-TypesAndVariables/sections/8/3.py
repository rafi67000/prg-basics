###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def celsius_to_fahrenheit(celsius):
    return celsius * (9/5) + 32


celsius = int(input())
kelvin = celsius_to_kelvin(celsius)
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"""
Celsius: {celsius}
Kelvin: {kelvin}
Fahrenheit: {fahrenheit}
""")
