# Program wyswietla kraje z co najmniej 10 medalami.

medals = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}
] # medale poszczegolnych krajow

filter_func = lambda x: x["gold"] + x["silver"] + x["bronze"] >= 10

result = list(filter(filter_func, medals)) # wybor krajow

print("COUNTRIES WITH AT LEAST 10 MEDALS")

for country in result:
    print(f'{country["country"]}: {country["gold"]},{country["silver"]},{country["bronze"]}') # wyswietlenie medali
