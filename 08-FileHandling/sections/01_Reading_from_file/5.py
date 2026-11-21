###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file: # with żeby plik został automatycznie zamknięty
    i = 0 # index
    for line in file: # iteracja
        i += 1 # zwiększenie indeksu
        print(f"{i}. {line}", end="")

    print("")  # pusta linia żeby było ładniej