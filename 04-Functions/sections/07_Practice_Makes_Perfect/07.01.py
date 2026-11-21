# 1. Nazwa miesiąca
def month(n):
    # n – numer miesiąca od 1 do 12
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    if 1 <= n <= 12:
        return months[n - 1]  # Indeksy listy zaczynają się od 0
    return "Unknown month"

month_number = int(input("Enter month number: "))  # month_number – numer od użytkownika
print("The name of month", month_number, "is", month(month_number))
