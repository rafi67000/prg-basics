# 26. Najdłuższa seria takich samych wyników rzutu kostką
def longest_dice_run(dice):
    # dice – tekst z wynikami kolejnych rzutów
    if dice == "":
        return 0
    longest = 1  # longest – najdłuższa znaleziona seria
    current = 1  # current – długość aktualnej serii
    best_face = int(dice[0])  # best_face – wynik kostki z najdłuższej serii
    current_face = dice[0]  # current_face – aktualnie powtarzający się wynik

    for i in range(1, len(dice)):
        if dice[i] == current_face:
            current += 1
        else:
            current_face = dice[i]
            current = 1

        if current > longest:
            longest = current
            best_face = int(current_face)

    return best_face

print(longest_dice_run("5233165554211"))
print(longest_dice_run("2133"))
