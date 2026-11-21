# slownik
person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123444321", "mobile": "777888999"}
}

# Wyświetlenie imienia.
print(person["name"])

# Wyświetlenie wszystkich hobby
print(person["hobby"])

# Wyświetlenie całego słownika.
print(person)
print()

# Zmiana nazwiska w slowniku
person["surname"] = "Nowak"

# Zmiana statusu małżeńskiego na odwrotny
person["married"] = not person["married"]

# Dodanie nowej pary klucz 'gender' wartosc 'male'
person["gender"] = "male"

# Hobby jest listą, więc dodajemy nowe hobby do niej.
person["hobby"].append("bicycle")

# 'phone' to slownik w slowniku - dodajemy do niego nową pare "work"
person["phone"]["work"] = "313131444"

# Wyświetlenie całej zawartości
for key, value in person.items(): # iterowanie po parach (tuple/krotka)
    print(f"{key}: {value}")
