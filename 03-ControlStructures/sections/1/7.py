#oblicza wynagrodzenie pracownika z premią

basic_salary = 5000  #wynagrodzenie podstawowe
total_salary = 0  #wynagrodzenie całkowite
bonus = 0.15  #premia wynosi 15%

is_bonus = input('Does the employee receive a bonus? (Y/N): ') == 'Y'

#jeżeli pracownik otrzymuje premię
if is_bonus:
    total_salary = basic_salary + basic_salary * bonus
else:
    total_salary = basic_salary

#wynik
print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')