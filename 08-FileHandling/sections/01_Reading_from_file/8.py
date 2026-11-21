###
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

file_contents = read_from_file('pets.txt')

print(file_contents) # print całości

words = file_contents.split(' ') # rozdzielenie słow
total = len(words) # ilosc elementow

print("Total words:", total)