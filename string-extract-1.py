# This script extract the portion of a given string
# and convert it into a floating point number.

# the given string
str = 'X-DSPAM-Confidence: 0.8475 '

# personal algorithm
colon_position = str.find(':')
space2_position = str.find(' ', colon_position + 2)
extracted_string = str[colon_position + 2 : space2_position]
number = float(extracted_string)
print(number)
