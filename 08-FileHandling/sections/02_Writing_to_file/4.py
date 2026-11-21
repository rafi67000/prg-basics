###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

with open(employees_file, mode='r') as file:
    employees_file_content = file.read() # odczyt

lines = employees_file_content.splitlines() # rozdzielenie linii

with open(position_file, mode= 'w') as file: # zapis

    for line in lines:

        elements = line.split(",") # nazwisko, imie, praca

        if (job_title in elements[2]): # tylko dla software engineer

            file.write(elements[1] + " " + elements[0] + "\n") # print imie nazwisko i \n dla nowej linii