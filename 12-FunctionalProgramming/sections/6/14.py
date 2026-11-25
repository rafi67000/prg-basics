# Program oblicza procent zle napelnionych butelek.

def check_filling(capacity, tolerance):
    difference = capacity * tolerance / 100 # dopuszczalna roznica
    return lambda x: abs(x - capacity) > difference # sprawdzenie napelnienia


capacity = 500 # pojemnosc butelki
tolerance = 2 # tolerancja w procentach
bottles = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509] # napelnienie butelek

incorrect = list(filter(check_filling(capacity, tolerance), bottles)) # zle napelnione butelki
percentage = len(incorrect) / len(bottles) * 100 # obliczenie procentu

print(f"Bottle capacity:    {capacity}ml")
print(f"Filling tolerance:  {tolerance}%")
print("Filled bottles:    ", ",".join(map(str, bottles)))
print(f"Incorrectly filled: {percentage:.0f}%")
