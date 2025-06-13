# This script extract the portion of a given string
# and convert it into a floating point number.

# the given string
str = 'X-DSPAM-Confidence: 0.8475 '

# personal algorithm
colon_position = str.find(':')
piece = str[colon_position + 1 : ]
# extracted_string = piece.strip()
# number = float(extracted_string)
number = float(piece)
print(number)
