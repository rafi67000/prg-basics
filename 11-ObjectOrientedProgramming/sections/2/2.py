class Song:
    def __init__(self, artist, title, album, year):
        self.artist = artist # wykonawca
        self.title = title # tytul utworu
        self.album = album # nazwa albumu
        self.year = year # rok wydania

    # Przedstawienie utworu w postaci String
    def __str__(self):
        return f"Performer: {self.artist}\nTitle:     {self.title}\nAlbum:     {self.album}\nYear:      {self.year}"


# stworzenie utworow
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Song("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)

# wyswietlenie utworow
print(song1)
print()
print(song2)