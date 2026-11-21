required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

# A.issubset(B) -> True, jeśli KAŻDY element A znajduje się w B.
# Pytamy: czy wymagane uprawnienia zawierają się w uprawnieniach użytkownika?
has_permissions = required_permissions.issubset(user_permissions)
print(has_permissions)  # zwroci false bo nie ma permisji execute
