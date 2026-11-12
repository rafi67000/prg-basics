#ankieta z trzema pytaniami

print('SURVEY')

#pobranie odpowiedzi na pytania
computer_science = input('Are you interested in computer science? (y/n): ')
computer_games = input('Do you like playing computer games? (y/n): ')
instagram = input('Do you have an Instagram account? (y/n): ')

#zamiana odpowiedzi tekstowych na wartości logiczne
computer_science = computer_science == 'y'
computer_games = computer_games == 'y'
instagram = instagram == 'y'

#wyświetlenie wyników ankiety
print('\nSURVEY RESULTS')

if computer_science:
    print('Interested in computer science: Yes')
else:
    print('Interested in computer science: No')

if computer_games:
    print('Playing computer games: Yes')
else:
    print('Playing computer games: No')

if instagram:
    print('Has an Instagram account: Yes')
else:
    print('Has an Instagram account: No')