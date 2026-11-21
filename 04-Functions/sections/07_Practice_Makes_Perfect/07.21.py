# 21. Hasło: minimum 6 znaków i bez powtarzających się znaków
def is_valid_password(password):
    # password – hasło do sprawdzenia
    return len(password) >= 6 and len(password) == len(set(password))

print(is_valid_password("ax15"))
print(is_valid_password("book123"))
print(is_valid_password("A2water3"))
print(is_valid_password("qwerty"))
print(is_valid_password(""))
