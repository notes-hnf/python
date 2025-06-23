# This script prompts the user to provide a filename,
# it will use 'clown.txt' if there is no filename provided.
# It counts and shows the top 5 most repeated words
# in the chosen file.

# prompt the user to provide a filename
# and use 'clown.txt' as a fallback filename
filename = input ('Please enter a filename: ')
if len(filename) < 1:
    filename = 'clown.txt'
filehandle = open(filename)

# count every line and make a word histogram
# by saving all the counted times in a dictionary called 'counts'
counts = dict()
for line in filehandle:
    line = line.rstrip()
    word_list = line.split()
    for word in word_list:
        counts[word] = counts.get(word, 0) + 1

# make a sorted list depending on the counted times
# and show the top 5 most repeated words
sorted_list = sorted([(val, key) for key, val in counts.items()], reverse=True)
for (val, key) in sorted_list[:5]:
    print(key, val)

