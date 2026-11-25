#
# Obliczanie sredniej predkosci
# Z wykorzystaniem funkcji anonimowej (lambda)
#

avg_speed = lambda distance, hours, minutes: distance / (hours + minutes / 60) # srednia predkosc

distance = float(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

speed = avg_speed(distance, hours, minutes) # obliczenie predkosci

print(f"Average speed: {speed:.1f} km/h")