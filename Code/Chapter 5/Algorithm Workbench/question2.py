def main():
	keep_going = 'y'

	while keep_going == 'y' or keep_going == 'Y':
		number1 = float(input('Enter number 1: '))
		number2 = float(input('Enter number 2: '))
		total = number1 +number2
		print('Total',total)
		keep_going = input('Would you like to do another set? (y/n): ')
main()
