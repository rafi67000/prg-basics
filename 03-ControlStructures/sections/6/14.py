#sprawdza czy osoba jest dobrym influencerem

facebook = True
twitter = False
instagram = True

#liczy ilość posiadanych kont
accounts = 0

if facebook:
    accounts += 1

if twitter:
    accounts += 1

if instagram:
    accounts += 1

#sprawdza czy osoba ma minimum dwa konta
if accounts >= 2:
    print('You are a good influencer!')
else:
    print('You are not a good influencer.')