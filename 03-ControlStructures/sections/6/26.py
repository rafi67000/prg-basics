#sprawdzanie kodu PIN w terminalu płatniczym

correct_pin = '0805'  #prawidłowy PIN
attempts = 0  #licznik nieudanych prób
max_attempts = 3  #maksymalna liczba prób

#pętla działa dopóki nie przekroczymy limitu prób
while attempts < max_attempts:

    pin = input('Enter the PIN code: ')

    #sprawdza poprawności kodu
    if pin == correct_pin:
        print('Correct PIN. Access granted.')
        break
    else:
        print('Incorrect...')
        attempts += 1

#sprawdza czy karta została zablokowana
if attempts == max_attempts:
    print('Sorry, your payment card has been blocked.')