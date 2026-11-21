import re

# get username and password from keyboard
username = input("Enter username: ")
password = input("Enter password: ")

# regular expression patterns
username_pattern = r'^[a-z]{6,}$'
password_pattern = r'^[a-zA-Z0-9_]{8,}$'

# check username
if re.fullmatch(username_pattern, username):
    print("Username is valid!")
else:
    print("Username is invalid!")

# check password
if re.fullmatch(password_pattern, password):
    print("Password is valid!")
else:
    print("Password is invalid!")

