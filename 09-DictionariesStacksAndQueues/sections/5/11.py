import json
import os

# Wczytanie zapisanych głosów
# Przy pierwszym uruchomieniu plik może jeszcze nie istnieć
if os.path.exists('voting.json'):
    with open('voting.json', encoding='utf-8') as file:
        votes = json.load(file)
else:
    votes = {}

# Dodanie głosu
name = input('Name of the person you are voting for: ').strip()
if name:
    # Istniejącej osobie zwiększamy liczbę głosów
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1
else:
    print('Empty name - no vote recorded.')

# Zapisanie głosów do pliku
with open('voting.json', 'w', encoding='utf-8') as file:
    # Zapisujemy słownik w czytelnej postaci JSON
    json.dump(votes, file, indent=4, ensure_ascii=False)

for name in votes:
    print(name, ':', votes[name])
