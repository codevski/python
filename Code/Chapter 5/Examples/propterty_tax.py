# This program displays propterty taxes.

# TAX_FACTOR is used as global constant
# for the tax factor.
TAX_FACTOR = 0.0065

# The main function.
def main():
	# Get the first lot number
	print('Enter the propterty lot number')
	print('or enter 0 to end.')
	lot = int(input('Lot Number: '))

	# Continue the processing as long as the user
	# does not enter lot number 0
	while lot != 0:
		# Show the tax for the property
		show_tax()

		# get the next lot nunber.
		print('Enter the next lot number or')
		print('enter 0 to end.')
		lot = int(input('Lot Number: '))

# The show_tax function gets a propterty's
# value and displays its tax.
def show_tax():
	# Get the property value.
	value = float(input('Enter the property value: '))

	# Calculate the property's tax.
	tax = value * TAX_FACTOR

	# Display the tax.
	print('Property tax: $', format(tax, ',.2f'), sep='')

# Call the main function.
main()

