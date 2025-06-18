# This script extracts the day information from every line
# that starts with "From ".

mailbox_file = open('mbox-short.txt')
for line in mailbox_file:
    line = line.rstrip()
    word_list = line.split()
    if len(word_list) < 3 or word_list[0] != 'From':
        continue
    chosen_word = word_list[2]
    print(chosen_word)
