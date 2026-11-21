###
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

# reads the entire file and splits lines into array
file_content = read_from_file('car_park.txt') # odczyt pliku
file_lines = file_content.splitlines() # rozdzielenie linii

# calculates the total number of cars parked
total = 0

for line in file_lines:
   total += int(line) # sumowanie

print('Total cars parked:', total)