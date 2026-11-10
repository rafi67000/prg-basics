###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
print(f"Cuboid: {a}x{b}x{c}")
print("Volume:", a * b * c)
print("Surface area:", a * b * 2 + a * c * 2 + b * c * 2)