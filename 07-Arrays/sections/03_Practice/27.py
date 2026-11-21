# Wykres sin(x) dla kątów od 0 do 360 stopni
import matplotlib.pyplot as plt
import math

x = []
y = []

# Kąty w stopniach
for degree in range(0, 361):
    x.append(degree)

# Funkcja sin() przyjmuje argument w radianach
for degree in x:
    y.append(math.sin(math.radians(degree)))

plt.plot(x, y)
plt.show()
