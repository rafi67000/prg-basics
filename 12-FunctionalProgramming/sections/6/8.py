# Program wyswietla wyniki studentow dla roznych progow.

def min_pts(limit):
    return lambda pts: pts >= limit # sprawdzenie progu


scores = [37, 51, 44, 23, 78, 92, 39, 84, 83, 51] # wyniki studentow
limits = [70, 40, 30] # progi zaliczenia

for limit in limits:
    result = list(filter(min_pts(limit), scores)) # wybor zaliczonych wynikow
    print(f"Min {limit} pts: {result}")
