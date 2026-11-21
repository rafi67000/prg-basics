# 20. Akronim, czyli pierwsze litery wszystkich słów
def acronym(name):
    # name – tekst zawierający słowa
    words = name.split()  # words – lista słów oddzielonych spacjami
    result = ""  # result – akronim z pierwszych liter
    for word in words:
        result += word[0].upper()
    return result

print(acronym("Internet of Things"))
print(acronym("For Your Information"))
print(acronym("Python"))
