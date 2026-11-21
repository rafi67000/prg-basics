# Zadanie: suma cyfr liczby
def sum_digits(number):
    # number – liczba, której cyfry sumujemy
    number = abs(number)  # Usunięcie ewentualnego minusa
    text = str(number)    # text – liczba zamieniona na tekst
    total = 0             # total – suma cyfr, początkowo 0

    for digit in text:    # digit – kolejna cyfra w postaci tekstu
        total += int(digit)  # Zamiana cyfry na int i dodanie do sumy

    return total

any_number = int(input("Enter integer number: "))  # any_number – liczba od użytkownika
result = sum_digits(any_number)  # result – suma cyfr podanej liczby
print("Sum of digits:", result)
