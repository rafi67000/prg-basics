# Funkcja zwraca napis składający się z n gwiazdek
def star(n):
    result = ""
    for i in range(n):
        result += "*"
    return result

arr = [2, 6, 4, 9, 7]
for value in arr:
    print(value, ":", star(value))
