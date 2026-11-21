# 10. n gwiazdek oddzielonych ukośnikiem
def asterisks(n):
    # n – liczba gwiazdek
    return "/".join(["*"] * n)  # join łączy gwiazdki znakiem /

print(asterisks(4))
print(asterisks(1))
