#oblicza liczbe dni w podanym miesiącu

month = int(input('Enter month number (1..12): '))

#miesiące mające 31 dni
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31

#miesiące mające 30 dni
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30

#luty ma 28 dni
elif month == 2:
    days = 28
else:
    days = 0

if days == 0:
    print('Incorrect month number')
else:
    print(f'Month {month} has {days} days')