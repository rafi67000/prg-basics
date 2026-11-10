import random

rolled = random.randint(1, 6)

print("Dice rolled: ", rolled)
print("Special number: ", rolled == 1 or rolled == 6)