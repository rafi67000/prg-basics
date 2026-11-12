#sprawdza poprawności loginu i hasła

login = 'joe'  #prawidłowy login
password = 'abcd'  #prawidłowe hasło

entered_login = input('Login: ')
entered_password = input('Password: ')

#oba warunki muszą być spełnione jednocześnie
if login == entered_login and password == entered_password:
    print('You are logged in')
else:
    print('Incorrect login or password!!')