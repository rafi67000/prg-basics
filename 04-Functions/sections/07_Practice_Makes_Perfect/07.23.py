# 23. Suma liczb podzielnych przez 2 i 3, ale nie przez 4
def selected_numbers_sum(x, y):
    # x, y – krańce przedziału domkniętego
    total = 0  # total – suma pasujących liczb
    for number in range(x, y + 1):
        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:
            total += number
    return total

print(selected_numbers_sum(1, 20))
print(selected_numbers_sum(10, 30))
