# This script prompts the user to provide their number of hours worked
# and the rate per hour, then calculates the total salary, with
# the ratio multiplied by 1.5 for an additional hour out of 40 hours.

number_hours = float(input('Please input your number of hours worked: '))
rate_per_hour = float(input ('Please input your rate per hour: '))

if number_hours <= 40:
    gross_pay = rate_per_hour * number_hours
else:
    gross_pay = rate_per_hour * 40 + rate_per_hour * 1.5 * (number_hours - 40)

print(f'Your total salary is: {gross_pay}.')
