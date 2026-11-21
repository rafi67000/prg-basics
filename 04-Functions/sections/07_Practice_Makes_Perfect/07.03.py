# 3. Sprawdzenie, czy liczba należy do przedziału domkniętego
def in_range(number, x, y):
    # number – sprawdzana liczba; x, y – granice przedziału
    return x <= number <= y

number = int(input("A number: "))  # number – liczba wpisana przez użytkownika
print("Number", number, "in the range <2,15>:",
      "yes" if in_range(number, 2, 15) else "no")
