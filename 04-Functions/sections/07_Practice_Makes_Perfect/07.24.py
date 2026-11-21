# 24. Wstawianie myślnika pomiędzy znaki tekstu
def add_dashes(text):
    # text – tekst do rozdzielenia myślnikami
    return "-".join(text)

print(add_dashes("University"))
print(add_dashes("UE"))
print(add_dashes("x"))
print(add_dashes(""))
