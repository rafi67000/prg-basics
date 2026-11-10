###
# A program that, for a given speed in km/h,
# prints the speed in m/s
#

speed_kmh = int(input("Provide speed number (km/h): "))

speed_ms = speed_kmh * 1000 / 60 / 60
print(speed_kmh, "km/h = ", speed_ms, "m/s")