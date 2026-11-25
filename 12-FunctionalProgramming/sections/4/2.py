# Program wyswietla przekroczenia predkosci.

speeds = [48, 47, 54, 50, 42, 68, 39, 46] # zmierzone predkosci
limit = 50 # limit predkosci

speed_filter = lambda speed: speed > limit

too_fast = list(filter(speed_filter, speeds)) # przekroczenia limitu

print(f"Recorded values: {speeds}") # wszystkie predkosci
print(f"Speed too high: {too_fast}") # za duze predkosci
