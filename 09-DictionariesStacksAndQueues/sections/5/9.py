import csv

# Wczytanie nazw województw
provinces = {}
with open('province.csv', encoding='utf-8') as file:
    # Każdy wiersz CSV zawiera literę i nazwę województwa
    for row in csv.DictReader(file):
        provinces[row['Letter']] = row['Name']

# Przygotowanie liczników
counts = {}
for letter in provinces:
    counts[letter] = 0

# Zliczanie samochodów
unknown = 0
with open('vehicle.txt', encoding='utf-8') as file:
    for line in file:
        # Usuwamy spacje i znak końca linii
        plate = line.strip()
        if plate:
            # Pierwsza litera tablicy określa województwo
            letter = plate[0]
            if letter in counts:
                counts[letter] += 1
            else:
                unknown += 1

# Wyświetlenie wyników od największej liczby
for letter in sorted(counts, key=counts.get, reverse=True):
    print(provinces[letter], counts[letter])
print('Total:', sum(counts.values()))
if unknown > 0:
    print('Unrecognized plates:', unknown)
