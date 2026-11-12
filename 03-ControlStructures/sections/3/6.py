#sprawdza czy podany dzień istnieje w danym miesiącu

month = int(input('Enter month number (1..12): '))
day = int(input('Enter the day number of the month: '))

day_ok = False  #początkowo zakładamy że dzień jest niepoprawny

#sprawdza miesiące mające 31 dni
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if day >= 1 and day <= 31:
        day_ok = True

#sprawdzenie miesięcy mających 30 dni
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day >= 1 and day <= 30:
        day_ok = True

#sprawdzenie lutego
elif month == 2:
    if day >= 1 and day <= 28:
        day_ok = True

#komunikat
message = f'Day {day} for the month {month}'

if day_ok:
    print(f'{message} is correct')
else:
    print(f'{message} is incorrect')