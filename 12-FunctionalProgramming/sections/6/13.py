# Program tworzy wykres liczby medali zdobytych przez kraje.

import matplotlib.pyplot as plt # biblioteka do wykresow

medals = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}
] # lista medali

country_func = lambda x: x["country"] # nazwy krajow
sum_func = lambda x: x["gold"] + x["silver"] + x["bronze"] # suma medali

countries = list(map(country_func, medals)) # nazwy krajow
totals = list(map(sum_func, medals)) # suma medali

plt.bar(countries, totals) # wykres slupkowy
plt.title("Olympic medals") # tytul wykresu
plt.xlabel("Country") # opis osi X
plt.ylabel("Number of medals") # opis osi Y
plt.show() # wyswietlenie wykresu
