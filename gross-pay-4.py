# This script prompts the user to provide their number of hours worked,
# their rate per hour, and calculates the total salary, with each
# additional hour out of 40 hours, the rate is multiplied by 1.5.
# However, in this script, we make use of 'function'.

number_of_hours = input('Please input your number of hours worked: ')
rate_per_hour = input ('Please input your rate per hour: ')

def computepay(rate_per_hour, number_of_hours):
    try:
        rate_per_hour = float(rate_per_hour)
        number_of_hours = float(number_of_hours)
    except:
        print('Error! Please input a valid number!')
        quit()

    if number_of_hours <= 40:
        total_salary = rate_per_hour * number_of_hours
    else:
        total_salary = rate_per_hour * 40 + rate_per_hour * 1.5 * (number_of_hours - 40)
    return total_salary

total_salary = computepay(rate_per_hour, number_of_hours)
print(f'The final total salary is: {total_salary}.')
