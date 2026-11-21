###
# Prints employees employed in a specified position.
#
def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

file_contents = read_from_file(file_name) # odczyt z  pliku

lines = file_contents.splitlines() # rozdzielenie linii

index = 0

for line in lines:
    if job_title in line:
        index += 1 # zwiekszenie indeksu o 1

        elements = line.split(",") # rozdzielenie wartosci

        employee = elements[1] + " " + elements[0] # imie + nazwisko

        print(f"{index}. {employee}")