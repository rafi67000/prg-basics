# Moduł do przeliczania jednostek długości

def m_to_cm(n):
    # n – liczba metrów; wynik to centymetry
    return n * 100

def cm_to_m(n):
    # n – liczba centymetrów; wynik to metry
    return n / 100

def cm_to_inches(n):
    # n – liczba centymetrów; 1 cal = 2.54 cm
    return n / 2.54

def feet_inches_to_cm(feet, inches):
    # feet – liczba stóp; inches – dodatkowe cale
    total_inches = feet * 12 + inches  # total_inches – cała długość w calach
    return total_inches * 2.54  # Zamiana cali na centymetry

if __name__ == "__main__":
    print(f"2 m = {m_to_cm(2)} cm")
    print(f"532 cm = {cm_to_m(532)} m")
    print(f"10 cm = {cm_to_inches(10):.2f} inches")
    print(f"5 feet 8 inches = {feet_inches_to_cm(5, 8):.2f} cm")
