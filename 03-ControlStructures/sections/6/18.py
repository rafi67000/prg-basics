#określanie położenia punktu w układzie współrzędnych

x = int(input('Enter x: '))
y = int(input('Enter y: '))

#sprawdzenie położenia punktu
if x > 0 and y > 0:
    print(f'Point P({x},{y}) is in the first quadrant of the coordinate system')
elif x < 0 and y > 0:
    print(f'Point P({x},{y}) is in the second quadrant of the coordinate system')
elif x < 0 and y < 0:
    print(f'Point P({x},{y}) is in the third quadrant of the coordinate system')
elif x > 0 and y < 0:
    print(f'Point P({x},{y}) is in the fourth quadrant of the coordinate system')
elif x == 0 and y == 0:
    print('Point is at position (0,0)')
elif x == 0:
    print('Point is on the Y axis')
else:
    print('Point is on the X axis')