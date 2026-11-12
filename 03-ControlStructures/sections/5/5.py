#sumowanie liczb i obliczanie ich średniej
#program kończy działanie po wpisaniu 0

total_sum = 0  #suma wszystkich liczb
counter = 0  #licznik wprowadzonych liczb

while True:
    number = int(input('Enter a number (0 to stop): '))

    #zakończenie pętli po wpisaniu 0
    if number == 0:
        break

    #dodanie liczby do sumy
    total_sum += number

    #zwiększenie licznika liczb
    counter += 1

#wyświetlenie sumy
print(f'The total sum of the numbers is: {total_sum}')

#obliczenie średniej jeśli podano przynajmniej jedną liczbę
if counter > 0:
    average = total_sum / counter
    print(f'The arithmetic mean is: {average}')
else:
    print('No numbers were entered.')