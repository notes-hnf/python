# This script prompts the user to provide a filename,
# then reads through and prints the content of the file
# (line by line) all in upper case.

file_name = input('Please enter a filename: ')
try:
    file_handle = open(file_name)
except:
    print('No file found with the given filename!')
    quit()
for line in file_handle:
    line_uppercase = line.rstrip().upper()
    print(line_uppercase)
