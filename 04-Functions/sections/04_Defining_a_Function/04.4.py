# Zadanie: nazwa dnia tygodnia
def day_name(day_number):
    # day_number – numer dnia od 1 do 7
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]  # days – nazwy dni tygodnia
    if 1 <= day_number <= 7:
        result = days[day_number - 1]  # result – nazwa wybranego dnia
    else:
        result = "Unknown day"
    return result

print("Day 5:", day_name(5))
print("Day 3:", day_name(3))
print("Day 7:", day_name(7))
