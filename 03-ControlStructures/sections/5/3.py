#wyświetla powitanie

name = ''  #początkowo imię jest puste

#pętla działa dopóki użytkownik nie wpisze imienia
while name == '':
    name = input('Enter your name: ')

# Wyświetlenie powitania
print(f'Hello {name}')