class C:
    def __init__(self, sectors):
        self.sectors = sectors # sektory i liczba kibicow

    def m1(self, s, n):
        self.sectors[s] = n # ustawienie liczby kibicow

    def m2(self, s):
        total = 0 # suma kibicow
        for sector in s:
            if sector in self.sectors:
                total += self.sectors[sector] # dodanie kibicow z sektora
        return total


stadium = C({"A": 120, "D": 150, "G": 90, "K": 110})
stadium.m1("G", 130)
print(stadium.m2("GD"))
print(stadium.m2("KEJ"))
