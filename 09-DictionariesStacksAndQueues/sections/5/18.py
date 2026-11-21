import json

# Wczytanie danych psów
with open('dogs.json', encoding='utf-8') as file:
    dogs = json.load(file)

# Wyświetlenie psów młodszych niż 5 lat
for dog in dogs:
    # Pomijamy psy mające 5 lat lub więcej
    if dog['age'] < 5:
        for key in dog:
            print(key, ':', dog[key])
        print()
