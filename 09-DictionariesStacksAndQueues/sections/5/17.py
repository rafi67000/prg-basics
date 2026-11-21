import json

# Wczytanie listy miast
with open('cities.json', encoding='utf-8') as file:
    # Plik zawiera listę słowników z danymi miast
    cities = json.load(file)

# Wyświetlenie informacji o miastach
for city in cities:
    # Wypisujemy kolejne informacje o mieście
    for key in city:
        print(key, ':', city[key])
    print()
