PERCENT = 0.60
TAX = 0.64

def main():
	property_value = float(input('Enter Property Value: $'))
	calc(property_value)

def calc(value):
	assessment = value * PERCENT
	tax = assessment / 100 * TAX
	print('Your Assessment value: $', format(assessment, ',.2f'), sep='')
	print('Tax: $', format(tax, ',.2f'), sep='')

main()
