# 9. Czy przynajmniej jedna z trzech liczb jest ujemna?
def has_negative(n1, n2, n3):
    # n1, n2, n3 – trzy sprawdzane liczby
    return n1 < 0 or n2 < 0 or n3 < 0

print(has_negative(11, 6, -4))
print(has_negative(5, 4, 14))
