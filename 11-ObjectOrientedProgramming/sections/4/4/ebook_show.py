from ebook import Ebook # import klasy

book = Ebook("The Hobbit", "J.R.R. Tolkien", 300)
book.open() # otwarcie ksiazki
book.show_status()
book.next_page()
book.next_page()
book.next_page()
book.previous_page()
book.show_status()
book.close() # zamkniecie ksiazki
book.next_page()
book.previous_page()
