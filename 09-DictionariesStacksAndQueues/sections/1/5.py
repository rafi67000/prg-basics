# lista z slownikami
countries = [
    {"name": "Poland",  "population": 38000000},
    {"name": "Germany", "population": 83200000},
    {"name": "France",  "population": 67750000},
    {"name": "Spain",   "population": 47400000},
    {"name": "Italy",   "population": 59000000},
]

# Nagłówek tabeli: kolumna 1 wyrównana do lewej (10 znaków), kolumna 2 do prawej (12).
print(f"{'COUNTRY':<10}{'POPULATION':>12}")

# Kazdy element listy to slownik
for country in countries:
    # znowu wyrownanie kraju do lewej i populacji do prawej
    print(f"{country['name']:<10}{country['population']:>12}")
