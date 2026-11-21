###
# Makes a copy of a text file
#

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file) as original_file:
   content = original_file.read() # odczyt

# write the content to the target file (copy)
with open(target_file, "w") as target_file:
   target_file.write(content) # zapis