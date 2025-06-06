# This script prompts the user to provide their number of hours worked,
# their rate per hour, and calculates the gross salary.
# For each additional hour out of 40 hours, the rate per hour
# is multiplied by 1.5.
# However, in this script, the error will also be handled if
# the user gives a 'string' instead of a 'number' for their answer.

number_of_hours = input('Please input your number of hours worked: ')
rate_per_hour = input('Please input your rate per hour: ')

try:
    number_of_hours = float(number_of_hours)
    rate_per_hour = float(rate_per_hour)
except:
    print('Error! Please input a valid number!')
    quit()

if (number_of_hours <= 40):
    gross_salary = rate_per_hour * number_of_hours
else:
    gross_salary = rate_per_hour * 40 + rate_per_hour * 1.5 * (number_of_hours - 40)

print(f'The final gross salary is: {gross_salary}.')
