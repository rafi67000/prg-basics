# 2. Liczenie wystąpień litery w tekście
def count_letter(text, letter):
    # text – badany tekst; letter – szukana litera
    counter = 0  # counter – liczba znalezionych wystąpień
    for char in text:  # char – kolejny znak tekstu
        if char == letter:
            counter += 1
    return counter

sample_text = "You never get a second chance to make a first impression"
print("The number of letter 'e':", count_letter(sample_text, "e"))
