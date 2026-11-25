# Program wyswietla nazwiska pracownikow wielkimi literami.

employees = [
    ("Smith", "Lucy"),
    ("Jones", "Janet"),
    ("Lee", "Jerry"),
    ("Jackson", "Peter"),
    ("Johnson", "Rick"),
    ("Lewis", "Terry"),
    ("Clarke", "Robin")
] # lista pracownikow

format_func = lambda e: e[0].upper() + ", " + e[1]

result = list(map(format_func, employees)) # formatowanie danych

for employee in result:
    print(employee) # wyswietlenie pracownika
