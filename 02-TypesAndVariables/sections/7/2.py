###
# A program that checks whether the password length
# read from the keyboard is correct.
#
password = input('Enter password: ')
password_ok = len(password) >= 8
print(f'Password length is valid: {password_ok}')

passwords = [ "university", "peter123", "seven", "anna333" ]

for password in passwords:
    result = ""
    if len(password) >= 8:
        result = "valid"
    else:
        result = "invalid"

    print("Password: ", password, "is: ", result)