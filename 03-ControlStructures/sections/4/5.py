#szyforwanie tekstu za pomocą szyfru Cezara
#każdy znak zostaje przesunięty o jeden kod do przodu

plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # Odczytanie kodu znaku
    char_code = ord(char) #ord() zmienia znak ja jego kod liczbowy

    #dodanie jednego do kodu znaku
    new_char_code = char_code + 1

    #zamiana nowego kodu na znak
    new_char = chr(new_char_code) #chr() zamienia kod liczbowy z powrotem na znak

    #dodanie zaszyfrowanego znaku do tekstu
    encrypted_text = encrypted_text + new_char

print(plain_text)
print(encrypted_text)