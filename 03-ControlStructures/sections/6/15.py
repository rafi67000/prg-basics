#sprawdza poprawności numeru EAN-13

ean = input('Enter EAN-13 article number: ')

#sprawdza czy numer zawiera dokładnie 13 cyfr
#ean przechowuje numer produktu jako tekst
if len(ean) == 13 and ean.isdigit(): #len(ean) == 13 sprawdza długość numeru.
    print('Article number is correct') #isdigit() sprawdza, czy wszystkie znaki są cyframi.

    #sprawdza czy numer zaczyna się od 590
    if ean.startswith('590'):
        print('Article manufactured in Poland')
else:
    print('Incorrect article number')