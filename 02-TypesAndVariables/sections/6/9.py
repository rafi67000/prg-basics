# You can also check what character corresponds to the given code value. Use the available chr() function.
#
# Write a program that allows you to check what word is hidden in the following character codes:

list = [ 67, 111, 111, 108, 33 ]

for c in list:
    print(f"{c} is {chr(c)}")
