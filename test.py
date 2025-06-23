# This script will ...
#
#
#
#
#
#


filename = input('Please enter the filename: ')
if len(filename) < 1:
    filename = 'clown.txt'
filehandle = open(filename)

counts = dict()
for line in filehandle:
    line = line.rstrip()
    word_list = line.split()
    for word in word_list:
        counts[word] = counts.get(word, 0) + 1

most_repeated_word = None
biggest_count = None
for word,count in counts.items():
    if biggest_count is None or count > biggest_count:
        most_repeated_word = word
        biggest_count = count

print(f'The most repeated word is {most_repeated_word}, with a total of {biggest_count} times repeated.')
