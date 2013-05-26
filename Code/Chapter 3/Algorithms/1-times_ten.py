# Accept a value from the user
def main():
	number = int(input('Enter a number: '))
	times_ten(number)

# Calculation and Display
def times_ten(number):
	result = number * 10
	print('This number', result, 'has been x 10')

# Call the main function
main()
