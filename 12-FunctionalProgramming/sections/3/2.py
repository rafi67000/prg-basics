# Program liczy litery w kazdym slowie.

sentence = "I completely agree with you" # tekst
words = sentence.split() # podzial na slowa

amount = lambda word: len(word) # funkcja zliczajaca litery w slowie

result = list(map(amount, words)) # liczenie liter w całej liście

print(f"Text: {sentence}")
print(f"No. of letters in words: {result}")
