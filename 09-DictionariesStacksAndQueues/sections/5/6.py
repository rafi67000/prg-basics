# Podstawowe dane
basic_data = {
    "name": "Barbara",
    "age": 21
}

# Dodatkowe dane
advanced_data = {
    "status": "student",
    "married": False,
    "interest": ["reading", "swimming"]
}

# Łączenie dwóch słowników
person = basic_data.copy()
person.update(advanced_data)

# Wyświetlenie danych
for key in person:
    print(key, person[key])