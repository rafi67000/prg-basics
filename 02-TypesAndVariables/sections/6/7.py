###
# A program that prints a numerical representation of each letter of your name.
#

name = 'Rafał' # replace John with your name

index = -1
for char in name:
    index = index + 1
    print(f'The letter {name[index]} has a code {ord(name[index])}')

# print(f'The letter {name[0]} has a code {ord(name[0])}')
# print(f'The letter {name[1]} has a code {ord(name[1])}')