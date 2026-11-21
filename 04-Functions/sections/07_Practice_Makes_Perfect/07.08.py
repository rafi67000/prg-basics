# 8. Liczba ujemnych liczb parzystych w przedziale <x,y>
def negative_even_count(x, y):
    # x, y – granice przedziału
    counter = 0  # counter – liczba ujemnych liczb parzystych
    for number in range(x, y + 1):  # number – kolejna liczba w przedziale
        if number < 0 and number % 2 == 0:
            counter += 1
    return counter

print(negative_even_count(-7, 8))
print(negative_even_count(-1, 11))
