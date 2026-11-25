class C:
    def __init__(self, points):
        self.points = points # lista punktow

    def m(self, n):
        count = 0 # liczba punktow w pierwszej cwiartce
        for point in self.points:
            if point[0] > 0 and point[1] > 0:
                count += 1 # obie wspolrzedne dodatnie
        return count >= n


points = C([[2, 3], [1, 8], [-6, 4], [3, -7]])
print(points.m(2))
print(points.m(3))
