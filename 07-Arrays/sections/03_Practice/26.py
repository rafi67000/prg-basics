# Wykres funkcji f(x) = x^2 - 3
import matplotlib.pyplot as plt

x = []
y = []

# Tworzenie wartości x
for n in range(-100, 101):
    x.append(n)

# Obliczanie wartości y dla każdego x
for n in x:
    y.append(n * n - 3)

# Rysowanie wykresu
plt.plot(x, y)
plt.show()
