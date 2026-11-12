#maksymalna dozwolona prędkosc
speed_limit = 140

#Pobieramy prędkosc od użytkownika i zamieniamy tekst na liczbe calkowita int
car_speed = int(input('Enter car speed (km/h): '))

#sprawdza czy prędkość samochodu przekracza limit
if car_speed > speed_limit:
    #wyswietla informacje o przekroczeniu predkosci
    print(f'Your speed is {car_speed} km/h')
    print('Warning: speed limit exceeded!!')
