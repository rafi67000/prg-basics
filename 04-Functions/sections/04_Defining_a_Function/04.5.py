# Zadanie: alfabet fonetyczny ICAO
def icao(letter):
    # letter – pojedyncza litera do zamiany
    words = {
        "A": "Alfa", "B": "Bravo", "C": "Charlie", "D": "Delta",
        "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel",
        "I": "India", "J": "Juliett", "K": "Kilo", "L": "Lima",
        "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa",
        "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
        "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray",
        "Y": "Yankee", "Z": "Zulu"
    }  # words – słownik liter i odpowiadających im słów ICAO
    return words.get(letter.upper(), "???")  # upper() ignoruje wielkość litery

name = input("Enter your name: ")  # name – imię wpisane przez użytkownika
print("ICAO words:")
for char in name:  # char – kolejny znak imienia
    if char.isalpha():
        print(icao(char), end=" ")
print()
