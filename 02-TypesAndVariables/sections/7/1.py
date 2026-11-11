# People up to and including 26 years of age are exempt from paying taxes in Poland. Write a program that, based on the person's age entered from the keyboard, prints True if the person is exempt from paying taxes and prints False otherwise. Then, check if the program works correctly for the following data (age in years):

def is_exempt(_age):
    no_tax = _age <= 26
    print(f'Exemption from paying taxes: {no_tax}')

ages = [38, 27, 26, 22, 18]

###
# People up to and including 26 years of age are exempt
# from paying taxes in Poland. Write a program that,
# based on the person's age entered from the keyboard,
# prints True if the person is exempt from paying taxes
# and prints False otherwise.
#
age = int(input('Enter age: '))
is_exempt(age)

for age in ages:
    print(f"Age: {age}")
    is_exempt(age)