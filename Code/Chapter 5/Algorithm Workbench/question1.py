def main():
	# User enter a number
	number = int(input('Enter a number: '))

	product = number * 10

	while product < 100:
		print('The product is ', product)
		print('Its bellow 100')
		number = int(input('Enter another number: '))
		product = number * 10

	print('Product over 100')

main()
