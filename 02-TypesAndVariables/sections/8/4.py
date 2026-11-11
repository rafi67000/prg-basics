# Write a program, a unit converter, that prints your height both in cm and in feet and inches. Use ue the division operator without remainder and the operator calculating the remainder of the division.

###
# A program that prints your height both in cm and in feet and inches.
#

def convert(_cm):
    _inches = _cm / 2.54
    return divmod(_inches, 12)

cm = 177
# calculate the number of feet
feet, inches = convert(cm)

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')