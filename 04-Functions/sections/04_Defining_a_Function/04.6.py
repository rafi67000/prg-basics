# Zadanie: formatowanie czasu
def time_string(hours, minutes, time_format):
    # hours – godzina 0–23; minutes – minuty 0–59; time_format – "12" lub "24"
    if time_format == "24":
        return f"{hours:02d}:{minutes:02d}"  # :02d – minimum 2 cyfry, z zerem z przodu

    if time_format == "12":
        suffix = "am" if hours < 12 else "pm"  # suffix – oznaczenie przed/po południu
        display_hour = hours % 12  # display_hour – godzina w formacie 12-godzinnym
        if display_hour == 0:
            display_hour = 12
        return f"{display_hour}:{minutes:02d}{suffix}"

    return "Invalid time format"

print(time_string(15, 38, "24"))
print(time_string(8, 3, "24"))
print(time_string(0, 5, "24"))
print(time_string(11, 15, "12"))
print(time_string(0, 7, "12"))
print(time_string(7, 30, "12"))
print(time_string(12, 46, "12"))
print(time_string(13, 10, "12"))
print(time_string(19, 2, "12"))
