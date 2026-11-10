###
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#
import random

total = 0

for i in range(3):
    roll = random.randint(1,6)
    total += roll
    print(f"Dice roll #{i}: {roll}")

print("Sum: ", total)