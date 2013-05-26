def main():
	packages_weight = float(input('Enter Weight of packages: '))
	calc(packages_weight)

def calc(pw):
	if pw > 10:
		ship = 3.80
	elif pw > 6 and pw <= 10:
		ship = 3.70
	elif pw > 2 and pw <= 6:
		ship = 2.20
	elif pw <= 2:
		ship = 1.10

	print('Shipping charges: $', format(ship, ',.2f'), sep='')

main()
