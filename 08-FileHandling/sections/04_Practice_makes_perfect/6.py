def count_file(path):
    with open(path, encoding="utf-8") as f: # odczyt
        text = f.read()

    lines = len(text.splitlines()) # ilosc linii
    chars = len(text) # ilosc znakow
    words = len(text.split()) # ilosc slow
    return lines, chars, words # typ TUPLE

# Oczekiwanie na dane od uzytkownika
name = input("File name: ")

lines, chars, words = count_file(name) # typ tuple

print(f"Number of lines: {lines}")
print(f"Number of characters: {chars}")
print(f"Number of words: {words}")

