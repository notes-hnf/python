hours = input('Please enter number of hours: ')
rate = input ('Please enter the rate: ')
pay = float(rate) * float(hours)
pay = round(pay * 100) / 100 # to round the resulting pay to two decimal places
print('The pay is:', pay)

