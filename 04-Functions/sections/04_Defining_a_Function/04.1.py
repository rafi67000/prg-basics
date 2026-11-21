# Zadanie: pole trójkąta ze wzoru Herona
def triangle_area(a, b, c):
    # a, b, c – długości boków trójkąta
    s = (a + b + c) / 2  # s – połowa obwodu trójkąta
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # area – pole trójkąta
    return area

# Odczyt boków od użytkownika
side_a = float(input("Enter side a: "))  # side_a – pierwszy bok
side_b = float(input("Enter side b: "))  # side_b – drugi bok
side_c = float(input("Enter side c: "))  # side_c – trzeci bok
print("Triangle area:", triangle_area(side_a, side_b, side_c))

# Testy podane w zadaniu
print("Area 3, 4, 5:", triangle_area(3, 4, 5))
print("Area 5, 12, 13:", triangle_area(5, 12, 13))
print("Area 7, 24, 25:", triangle_area(7, 24, 25))
