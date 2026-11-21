import re

text = input("Enter text: ")

# Wyznaczenie wszystkich samoglosek
vowels = re.findall(r"[aeiou]", text, re.IGNORECASE) # r zeby python nie manipulował stringiem

print("Number of vowels:", len(vowels))