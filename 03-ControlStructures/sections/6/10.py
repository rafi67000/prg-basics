#oblicza wiek psa w psich latach

dog_age = float(input("Enter the dog's age in human years: "))

#dla pierwszych dwóch lat mnożymy wiek przez 10.5
if dog_age <= 2:
    result = dog_age * 10.5
else:
    #pierwsze dwa lata dają razem 21 lat
    #każdy kolejny rok dodaje 4 lata
    result = 2 * 10.5 + (dog_age - 2) * 4

print(f"The dog's age in dog's years is {result:g} years.") #:g w f-stringu wyświetla liczbę bez niepotrzebnego .0