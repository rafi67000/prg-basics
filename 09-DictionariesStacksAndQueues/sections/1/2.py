# dictionary
student = {
    'name': 'John',
    'age': 22,
    'major': 'Computer Science'
}

# odczyt ze slownika
print(student['name'])

# -dodanie nowej pary do slownika
student['grade'] = 'A'

# modyfikacja istniejacej pary
student['age'] = 23

# usuniecie pary
del student['major']
print(student)

#  nowy slownik
fruits = {'apple': 3, 'banana': 5, 'orange': 2}

# Pętla po samych kluczach
for fruit in fruits:
    print(fruit)

# Pętla po samych wartościach.
for count in fruits.values():
    print(count)

# Pętla po parach
for fruit, count in fruits.items(): # items zwraca pare KLUCZ x WARTOSC (tuple/krotka)
    print(f"The count of {fruit} is {count}")

# dictionary
person = {'name': 'Alice', 'age': 30}

# sprawdzanie czy klucz istnieje w slowniku
if 'name' in person:
    print("Name is present in the dictionary.")
else:
    print("Name is not present.")
