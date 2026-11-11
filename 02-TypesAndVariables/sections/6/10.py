###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters

print("Title in capital letters: " + movie.upper())

# print title in small letters

print("Title in lower case: " + movie.lower())

# print how many times the vowel "e" appears in the title

print("Count of vowels e: ", movie.count("e"))

# print where in the text is the word "Lord"
print('"Lord" at index:', movie.index("Lord"))

# print where in the text is the word "dragon"

if "dragon" in movie:
    print('"dragon" at index:', movie.index("dragon"))
else:
    print('"Dragon" is not in the text')