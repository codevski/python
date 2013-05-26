STATE_TAX = 0.04
COUNTY_TAX = 0.02

def main():
	total_sales = float(input('Enter total sales: $'))
	calc(total_sales)

def calc(total_sales):
	county_tax = total_sales * COUNTY_TAX
	state_tax = total_sales * STATE_TAX
	total_tax = county_tax + state_tax
	print('County Tax: $', format(county_tax, ',.2f'), sep='')
	print('State Tax: $', format(state_tax, ',.2f'), sep='')
	print('Total Tax: $', format(total_tax, ',.2f'), sep='')

main()
