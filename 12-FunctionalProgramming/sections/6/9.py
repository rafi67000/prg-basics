# Program wyswietla miasta z dodatnia temperatura.

temperatures = {
    "Krakow": 7,
    "Warszawa": -2,
    "Sopot": 4,
    "Koszalin": -1,
    "Opole": 3
} # temperatury w miastach

cities = list(filter(lambda city: temperatures[city] > 0, temperatures)) # cieple miasta

print("Cities with positive temperatures:", " ".join(cities)) # wyswietlenie miast
