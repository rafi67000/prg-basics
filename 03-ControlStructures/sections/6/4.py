#sprawdza długości nowego hasła

new_password = input('Enter new password: ')

#sprawdza czy hasło ma mniej niż 12 znaków
if len(new_password) < 12:
    print('Password too short (min. 12 chars)')
else:
    print('Password length is correct')