# Moduł funkcji do analizy tekstu

def word_count(text):
    # Liczba słów w tekście
    words = text.split()
    return len(words)

def words_longest_first(text):
    # Sortowanie słów od najdłuższego do najkrótszego
    words = text.split()
    words = sorted(words, key=len, reverse=True)
    return words

def words_alphabetically(text):
    # Sortowanie słów alfabetycznie
    words = text.split()
    words = sorted(words)
    return words
