
# Counts vowels in the text using while loop

text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0

i = 0  #indeks aktualnego znaku tekstu

# Count vowels in the text
while i < len(text):

    #sprawdza czy aktualny znak jest samogłoską
    if text[i] in vowels:
        vowel_count += 1

    #przejście do następnego znaku
    i += 1

print(f"The number of vowels in the text is: {vowel_count}")
