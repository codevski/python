# This program demostrates how a floating-point
# number can display as currency
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print('Your annual pay is $', \
	format(annual_pay, ',.2f'), \
	sep='')
