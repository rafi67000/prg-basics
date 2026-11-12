#wyświetla nazwy uczelni z dodatkową spacją między znakami

university = 'Krakow University of Economics'
university_expanded = ''  # nowy oddzielony tekst co powstanie 

#skakanie po każdym znaku nazwy uczelni
for char in university:
    university_expanded = university_expanded + char + ' '

#wyświetla obie wersje nazwy
print(university)
print(university_expanded)