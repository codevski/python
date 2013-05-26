SOFTWARE = 99

def main():
	packages = int(input('Enter the amount of packages purchased: '))
	calc(packages)

def calc(packages):
	if packages >= 100:
		print('You have 50% discount')
		total = packages * SOFTWARE * 0.50
		print('Your total price is: $', format(total, ',.2f'), sep='')
	elif packages >= 50 and packages <= 99:
		print('You have 40% discount')
		total = packages * SOFTWARE *  0.40
		print('Your total price is: $', format(total, ',.2f'), sep='')
	elif packages >= 20 and packages <= 49:
		print('You have 30% discount')
		total = packages * SOFTWARE * 0.30
		print('Your total price is: $', format(total, ',.2f'), sep='')
	elif packages >= 10 and packages <= 19:
		print('You have 20% discount')
		total = packages * SOFTWARE * 0.20
		print('Your total price is: $', format(total, ',.2f'), sep='')
	elif packages < 10:
		total = packages * SOFTWARE
		print('Your total price is: $', format(total, ',.2f'), sep='')
		print('No Discount')

main()
