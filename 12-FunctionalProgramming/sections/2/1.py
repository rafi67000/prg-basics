# Sprawdzenie minimalnej ilosci punktow

def min_pts(limit):
    def check(pts):
        return pts >= limit # sprawdzenie punktow
    return check # zwrocenie funkcji


print("=== MIN 50 PTS TO PASS ===")
assess_test = min_pts(50) # ustawienie progu
print(f"52 pts -> {assess_test(52)}")
print(f"39 pts -> {assess_test(39)}")

print("=== MIN 60 PTS TO PASS ===")
assess_test = min_pts(60) # zmiana progu
print(f"52 pts -> {assess_test(52)}")
print(f"39 pts -> {assess_test(39)}")
