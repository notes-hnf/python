# This script prompts user to provide a filename,
# then it counts every line in this file,
# and return the most repeated word with the associated count.

# prompt the user to provide filename and create filehandle
filename = input('Please enter the filename: ')
filehandle = open(filename)

count_dict = dict()
for line in filehandle:
    wordlist = line.split()
    for word in wordlist:
        count_dict[word] = count_dict.get(word, 0) + 1

most_repeated_word = None
biggest_count = None
for word,count in count_dict.items():
    if biggest_count is None or count > biggest_count:
        most_repeated_word = word
        biggest_count = count

print(most_repeated_word, biggest_count)


