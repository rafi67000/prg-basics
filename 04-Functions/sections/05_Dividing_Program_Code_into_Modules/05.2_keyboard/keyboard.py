# Moduł z funkcjami pobierającymi dane z klawiatury

def input_string(message):
    # message – tekst wyświetlany przed pobraniem danych
    value = input(message)  # value – tekst wpisany przez użytkownika
    return value

def input_integer(message):
    # message – komunikat; wynik funkcji będzie liczbą całkowitą
    value = input(message)  # value – wpisany tekst
    return int(value)  # Zamiana tekstu na int

def input_real(message):
    # message – komunikat; wynik funkcji będzie liczbą rzeczywistą
    value = input(message)  # value – wpisany tekst
    return float(value)  # Zamiana tekstu na float

def input_boolean(message):
    # message – komunikat; y oznacza True, n oznacza False
    value = input(message).lower()  # value – odpowiedź małymi literami
    return value == "y"  # Wynik True tylko wtedy, gdy wpisano y
