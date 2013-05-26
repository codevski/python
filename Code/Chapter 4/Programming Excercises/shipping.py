def main():
	package_weight = float(input('Enter the weight of the package in pounds: '))
	calc(package_weight)

def calc(pw):
	if pw < 11:
		if pw < 7:
			if pw < 3:
				ship_charge = 1.10
			else:
				ship_charge = 2.20
		else:
			ship_charge = 3.7
	else:
		ship_charge = 3.80

	print('Shipping Charges: $', format(ship_charge, ',.2f'), sep='')

main()
