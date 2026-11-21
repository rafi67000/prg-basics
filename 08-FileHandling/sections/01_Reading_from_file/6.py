###
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content

# reads the entire file
file_content = read_from_file('countries.txt')

# splits the entire file contents into lines
# and stores them in an array
file_lines = file_content.splitlines()

file_lines.sort() # sortowanie alfabetyczne

# prints the array
for line in file_lines: # iteracja
    elements = line.split(', ') # rozdzielenie kazdej linii na kraj, stolica, numer
    print(elements[0]) # print only country