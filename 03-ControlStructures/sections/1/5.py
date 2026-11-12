#Sprawdza czy test został zaliczony
#Test jest zaliczony po uzyskaniu co najmniej 50% punktów

total_tasks = 20  #Łączna liczba zadań
tasks_ok = int(input('Enter number of correctly completed tasks: '))

test_passed = False  #Początkowo zakładamy że test nie jest zaliczony

#Sprawdza czy liczba poprawnych odpowiedzi wynosi minimum 50%
if tasks_ok >= total_tasks * 0.5:
    test_passed = True

# Wyświetlenie wyniku testu
if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')