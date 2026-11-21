# 16. Usuwanie spacji z tekstu
def remove_spaces(sentence):
    # sentence – tekst, z którego usuwamy spacje
    return sentence.replace(" ", "")

print(remove_spaces("integrated development environment"))
print(remove_spaces("A programming language is a system of notation for writing computer programs"))
