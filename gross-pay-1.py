# This scripts helps the user to compute their gross pay,
# by asking the user to provide their number of working hours
# and their rate per hour.

number_hours = input('Please input your number of working hours: ')
rate_per_hour = input('Please input your rate per hour: ')
gross_pay = float(number_hours) * float(rate_per_hour)
print(f'Your gross pay is ${gross_pay}.')
