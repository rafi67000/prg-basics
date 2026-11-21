# Zwraca nazwę dnia tygodnia dla numeru 1-7
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]

# Wyświetlenie nazw dla podanych numerów
print(weekday(1))
print(weekday(4))
print(weekday(7))
