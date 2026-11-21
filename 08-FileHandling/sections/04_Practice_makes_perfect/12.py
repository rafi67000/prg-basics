# dictionary
GENRE_FILES = {
    "Fantasy": "books_fantasy.txt",
    "Historical": "books_historical.txt",
    "Romance": "books_romance.txt",
    "Classic": "books_classic.txt",
}

# odczyt z pliku
def read_books(path):
    with open(path, encoding="utf-8") as f:
        # rozdzielenie na linie
        lines = f.read().splitlines()

    return lines[0], lines[1:]          # naglowek, ksiazki

# FIltrowanie gatunkiem
def filter_by_genre(books, genre):
    selected = []
    for line in books:
        title, author, book_genre, year = line.split(",") # rozdzielenie linii na dane

        if book_genre == genre:
            selected.append(line) # dodawanie ksiazki bo jest z tego gatunku

    return selected # zwraca spelniajace warunek ksiazki

# zapis przefiltrowanych ksiazek
def save_books(path, header, books):
    with open(path, "w", encoding="utf-8") as f: # w - write

        f.write(header + "\n") # zapis naglowwka do pliku

        for line in books:
            f.write(line + "\n") # zapis ksiazki


# naglowek, ksiazki
header, books = read_books("books.csv")

for genre, filename in GENRE_FILES.items(): # iteracja po roznych gatunkach

     selected = filter_by_genre(books, genre) # filtrowanie przez gatunek

     save_books(filename, header, selected) # wywolanie zapisu

     print(f"{genre}: {len(selected)} books -> {filename}")