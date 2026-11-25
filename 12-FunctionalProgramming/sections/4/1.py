# Program wyswietla pracownikow z nazwiskiem na J.

employees = [
    "SMITH Lucy",
    "JONES Janet",
    "LEE Jerry",
    "JACKSON Peter",
    "JOHNSON Rick",
    "LEWIS Terry",
    "CLARKE Robin"
] # lista pracownikow

surname_filter = lambda e: e[0] == "J"

emp_J = list(filter(surname_filter, employees)) # filtrowanie nazwisk

for employee in emp_J:
    print(employee) # wyswietlenie pracownika
