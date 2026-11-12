#gra polegająca na zgadywaniu liczby

import random  #import biblioteki do losowania

#losowanie liczby od 1 do 100
number_to_guess = random.randint(1, 100)

user_guess = 0  #początkowa wartość zgadywanej liczby

print('Guess the number between 1 and 100!')

#petla działa dopóki użytkownik nie zgadnie liczby
while user_guess != number_to_guess:
    user_guess = int(input('Enter your guess: '))

    if user_guess < number_to_guess:
        print('Too low! Try again.')
    elif user_guess > number_to_guess:
        print('Too high! Try again.')
    else:
        print('Congratulations! You guessed the correct number.')