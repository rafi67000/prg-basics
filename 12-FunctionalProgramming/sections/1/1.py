###
# Calculates arithmetic mean of two integer numbers (średnia dwóch licz)
#
def mean(x,y):
   return (x + y) / 2

# takes two numbers from keyboard
n1 = float(input('Enter x: '))
n2 = float(input('Enter y: '))

# calculates arightmtic mean and print result
result = mean(n1, n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}.')