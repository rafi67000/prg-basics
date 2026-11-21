import json
import urllib.request

# Pobranie ostatnich 10 kursów euro z NBP
url = 'https://api.nbp.pl/api/exchangerates/rates/c/eur/last/10/?format=json'
# API zwraca kursy walut w formacie JSON
with urllib.request.urlopen(url) as response:
    data = json.load(response)

# Zapisanie danych do pliku
with open('euro.json', 'w', encoding='utf-8') as file:
    # Zapisujemy pobrane kursy do pliku
    json.dump(data, file, indent=4)

# Odczyt danych z pliku
with open('euro.json', encoding='utf-8') as file:
    data = json.load(file)

# Wyświetlenie kursów kupna i sprzedaży
print('Date           Buying Rate    Selling Rate')
print('==========================================')
# bid to kurs kupna, ask to kurs sprzedaży
for rate in data['rates']:
    print(rate['effectiveDate'], format(rate['bid'], '.4f'), format(rate['ask'], '.4f'))
