page_size=5

# wyswielt plik podzielony na strony
def page_file(path):
    with open(path, encoding="utf-8") as f: # odczyt
        lines = f.readlines()

    for start in range(0, len(lines), page_size):

        for line in lines[start:start + page_size]:  # wyswielt tylko te linie ktore sa przydzielone do tej strony
            print(line)

        if start + page_size < len(lines): # sprawdzanie czy jest kolejna strona
            input("Press Enter key...")

# glowna funkcja
page_file("it_company.csv")