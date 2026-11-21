import json

# Słownik z informacjami o filmie
favourite = {
    'title': 'The Matrix',
    'year': 1999,
    'directors': ['Lana Wachowski', 'Lilly Wachowski'],
    'genre': 'Sci-Fi',
    'rating': 8.7,
    'seen_multiple_times': True
}

# Zapisanie danych do pliku JSON
with open('favourite.json', 'w', encoding='utf-8') as file:
    # Zapisujemy dane filmu jako JSON z wcięciami
    json.dump(favourite, file, indent=4, ensure_ascii=False)

print('Saved to favourite.json')
