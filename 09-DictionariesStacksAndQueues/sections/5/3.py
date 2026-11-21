# Słownik z tłumaczeniami
translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

# Pobranie słowa od użytkownika
word = input('English word: ').strip().lower()

# Sprawdzenie czy słowo znajduje się w słowniku
if word in translations:
    print(word, '->', translations[word])
else:
    print('Translation is unavailable.')