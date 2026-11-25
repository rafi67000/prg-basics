# Program tworzy wykres temperatur w miastach.

import matplotlib.pyplot as plt # biblioteka do wykresow

temperatures = {
    "Krakow": 7,
    "Warszawa": -2,
    "Sopot": 4,
    "Koszalin": -1,
    "Opole": 3
} # temperatury w miastach

cities = list(map(lambda x: x[0], temperatures.items())) # nazwy miast
values = list(map(lambda x: x[1], temperatures.items())) # wartosci temperatur

plt.bar(cities, values) # wykres slupkowy
plt.title("Temperatures in cities") # tytul wykresu
plt.xlabel("City") # opis osi X
plt.ylabel("Temperature (C)") # opis osi Y
plt.show() # wyswietlenie wykresu
