def main():
	subtotal = float(input('Purchase Amount: $'))
	print('Subtotal: $', format(subtotal, ',.2f'), sep='')
	state_sales_tax(subtotal)
	county_tax(subtotal)

def state_sales_tax(subtotal):
	result	= subtotal * 0.04
	print('State Tax: $', format(result, ',.2f'), sep='')

def county_tax(subtotal):
	result = subtotal * 0.02
	print('County Tax: $', format(result, ',.2f'), sep='')

main()
