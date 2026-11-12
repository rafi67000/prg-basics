account_balance = 500  # stan konta
total_payment = float(input('Enter payment amount: '))  #kwota zakupów

#sprawdza czy na koncie są wystarczające środki
if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')