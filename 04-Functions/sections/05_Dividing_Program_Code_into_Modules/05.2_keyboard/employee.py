# Program wprowadzający i wyświetlający dane pracownika

import keyboard  # Import własnego modułu keyboard.py

# Pobieranie danych pracownika
first_name = keyboard.input_string("Enter first name: ")  # first_name – imię
last_name = keyboard.input_string("Enter last name: ")    # last_name – nazwisko
age = keyboard.input_integer("Enter age: ")               # age – wiek
salary = keyboard.input_real("Enter salary: ")             # salary – wynagrodzenie
is_salary_hidden = keyboard.input_boolean("Hide salary? (y/n): ")  # Czy ukryć pensję?

# Wyświetlanie danych pracownika
print("DATA RECORD")
print("===========")
print("Name:", first_name)
print("Last name:", last_name)
print("Age:", age)

if not is_salary_hidden:  # Pensja wyświetli się, jeśli użytkownik nie chce jej ukrywać
    print("Salary:", salary)
