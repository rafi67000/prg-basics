import re

with open("files.txt", encoding="utf-8") as f:  # odczyt
    for line in f:
        name = line.strip()  # usuniecie zbednych znakow

        if re.search(r"\.[^.\s]{4}$", name):  # jesli rozszerzenie zawiera 4 znaki np. html
            print(name)