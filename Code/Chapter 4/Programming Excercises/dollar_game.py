DOLLAR = 100

def main():
	pennies = int(input('Enter pennies: '))
	nickels = int(input('Enter nickels: '))
	dimes = int(input('Enter dimes: '))
	quarters = int(input('Enter quarters: '))
	calc(pennies, nickels, dimes, quarters)

def calc(p, n, d, q):
	total = p + n * 5 + d * 10 + q * 25

	if total == DOLLAR:
		print('Congrates!!!! You WIN!')
	elif total > DOLLAR:
		print('You are over the Dollar Mark')
	elif total < DOLLAR:
		print('Bellow Dollar')

main()
	
