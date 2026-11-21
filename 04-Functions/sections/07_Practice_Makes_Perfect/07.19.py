# 19. Różnica między największą i najmniejszą z trzech liczb
def max_min_difference(number1, number2, number3):
    # number1, number2, number3 – porównywane liczby
    return max(number1, number2, number3) - min(number1, number2, number3)

print(max_min_difference(7, 4, 9))
print(max_min_difference(2, 12, 8))
