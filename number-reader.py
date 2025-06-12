# This scripts reads numbers from user's input, until the user enters 'done'.
# It will print out the total, the count and the average of the given numbers.
# If the user enters anything other than a number, the mistake will be detected
# and an error message will be shown.

# initial values
total = 0.0
count = 0

# while loop
while True:
    user_input = input('Please enter a number: ')
    if user_input == 'done':
        break
    else:
        try:
            number = float(user_input)
            total += number
            count += 1
            average = total / count
            print(f'Total: {total}. Count: {count}. Average: {average}.')
        except:
            print('Invalid input! Please try again!')
