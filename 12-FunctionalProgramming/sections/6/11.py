# Program wyswietla studentow z wynikiem od 50 do 70 punktow.

test_results = [
    {"name": "Peter", "result": 27},
    {"name": "Anna", "result": 63},
    {"name": "Robert", "result": 92},
    {"name": "Paul", "result": 46},
    {"name": "Barbara", "result": 52}
] # wyniki studentow

filter_func = lambda x: 50 <= x["result"] <= 70

students = list(filter(filter_func, test_results)) # wybor wynikow

for student in students:
    print(student["name"], student["result"]) # imie i wynik
