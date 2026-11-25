# Sortowanie po dlugosci imienia

names = [
    "James",
    "Emily",
    "William",
    "Olivia",
    "Benjamin",
    "Sophia",
    "Henry"
] # lista imion

print("Unsorted list:")
for name in names:
    print(name) # wyswietlenie imienia

length = lambda name: len(name) # dlugosc imienia

sorted_names = sorted(names, key=length) # sortowanie po dlugosci (kryterium to funkcja length)

print("Sorted list:")
for name in sorted_names:
    print(name) # wyswietlenie posortowanego imienia
