# This program calculates sales commissions.
def main():
	# Create a variable to control the loop.
	keep_going = 'y'

	# Calculate a series of commissions.
	while keep_going == 'y':
		# Call the show_commission function to
		# display a salesperson's commission.
		show_commission()

		# See if the user wants to do another one.
		keep_going = input('Do you want to calculate another ' + \
							'commission (Enter y for yes or n for no): ')

# The show commission function gets the amount of
# sales and the commission rate, and then displays
# the amount of commission.
def show_commission()	:
	# get the salesperson's sales and commission rate.
	sales = float(input('Enter the amount of sales: '))
	comm_rate = float(input('Enter the commission rate: '))

	# Calculate the commission.
	commission = sales * comm_rate

	# Display the commission.
	print('The commission is $', \
			format(commission, ',.2f'), sep='')

# Call the main function
main()
