# Tekst do sprawdzenia
paragraph = "cat dog mouse cat rat cat mouse"

# Pusty słownik na liczbę wystąpień słów
counts = {}

# Liczenie wystąpień każdego słowa
for word in paragraph.split():
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

# Wyświetlenie wyników
for word in counts:
    print(word, counts[word])