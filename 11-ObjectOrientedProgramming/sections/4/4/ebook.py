class Ebook:
    def __init__(self, title, author, pages):
        self.title = title # tytul ksiazki
        self.author = author # autor
        self.pages = pages # liczba stron
        self.current_page = 1 # aktualna strona
        self.is_open = False # stan ksiazki

    def open(self):
        self.is_open = True # otwarcie ksiazki

    def close(self):
        self.is_open = False # zamkniecie ksiazki

    def next_page(self):
        if not self.is_open:
            print("Book is closed")
        elif self.current_page < self.pages:
            self.current_page += 1 # nastepna strona

    def previous_page(self):
        if not self.is_open:
            print("Book is closed")
        elif self.current_page > 1:
            self.current_page -= 1 # poprzednia strona

    def show_status(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Pages:", self.pages)
        print("Current page:", self.current_page)
