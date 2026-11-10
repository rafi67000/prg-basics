# r = 1 --> circumference = 6.28, area = 3.14
# r = 3 --> circumference = 18.84, area = 28.26

###
# Calculation of circle area and circumference
#

import math

def calculate(radius):

    # calculate area

    area = math.pi * (radius ** 2)

    # calculate circumference

    circumference = 2 * math.pi * radius

    # print results

    print(f'For radius={radius} the circumference is {circumference} and the area is: {area}')
    return circumference, area


radius = int(input('Enter radius: '))
calculate(radius)

for r in [1, 3]:
    calculate(r)
