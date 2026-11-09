###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#

print("Provide speed number (km/h):")

speed_kmh = int(input())

speed_ms = speed_kmh * 1000 / 60 / 60
print(speed_kmh, "km/h = ", speed_ms, "m/s")