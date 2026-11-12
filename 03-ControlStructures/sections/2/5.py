#kwartał roku na podstawie numeru miesiąca

month = int(input('Enter month number (1..12): '))

if month >= 10 and month <= 12:
    quarter = 4
elif month >= 7:
    quarter = 3
elif month >= 4:
    quarter = 2
elif month >= 1:
    quarter = 1
else:
    quarter = 0

if quarter == 0:
    print('Incorrect month number')
else:
    print(f'Month {month} is in quarter {quarter}')