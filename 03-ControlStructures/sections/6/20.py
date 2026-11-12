#zamiana liczby dziesiętnej na binarną

number = int(input('Enter decimal number: '))

original_number = number  #zapamiętanie początkowej liczby
binary = ''  #zmienna przechowująca wynik binarny

#obsługa liczby zero
if number == 0:
    binary = '0'

#dzielenie przez 2 i zapisywanie reszt
while number > 0:
    remainder = number % 2  #obliczenie reszty z dzielenia
    #remainder przechowuje resztę z dzielenia przez 2
    binary = str(remainder) + binary  #dodanie reszty na początku
    #str() zamienia resztę na tekst
    number = number // 2  #dzielenie całkowite przez 2

print(f'{original_number}(10) = {binary}(2)')