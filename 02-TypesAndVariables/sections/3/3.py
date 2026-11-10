###
# A program for swapping two varable values
#

x = 7
y = 34

print("Before swapping: x=", x, "y=", y)

# swap the values

temp = x  # additional, auxiliary variable
x = y
y = temp

print("After swapping: x=", x, "y=", y)

# Proper way to do that (ignorujac polecenie ze ma byc temp zmienna):

print("Before swapping: x=", x, "y=", y)
x, y = y, x
print("After swapping: x=", x, "y=", y)
