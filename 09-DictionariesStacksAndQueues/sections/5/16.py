import json

# Wczytanie danych komputera
with open('computer.json', encoding='utf-8') as file:
    # JSON zostaje wczytany jako słownik
    data = json.load(file)

# Wyświetlenie danych
for key in data:
    print(key, ':', data[key])
