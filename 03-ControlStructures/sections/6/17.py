#zamiana czasu z formatu 24-godzinnego na 12-godzinny

time = input('Enter time (24-hour format): ')

#podział czasu na godziny i minuty
hours = int(time[0:2]) #time[0:2] pobiera dwie pierwsze cyfry, czyli godzinę.
minutes = time[3:5] #time[3:5] pobiera minuty.

#ustalenie oznaczenia am lub pm
if hours >= 12:
    period = 'pm'
else:
    period = 'am'

#zamiana godziny na format 12-godzinny
if hours > 12:
    hours -= 12
elif hours == 0:
    hours = 12

print(f'Time in 12-hour format: {hours}:{minutes}{period}')