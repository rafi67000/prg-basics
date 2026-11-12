#sprawdza poprawności prędkości samochodu

car_speed = int(input('Enter car speed: '))

speed_limit_min = 40  #minimalna prędkość
speed_limit_max = 140  #maksymalna prędkość

#sprawdza czy prędkość mieści się w dozwolonym zakresie
if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print('Warning: invalid car speed!!')
else:
    print('Car speed is valid')