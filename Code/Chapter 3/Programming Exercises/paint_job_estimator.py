def main():
	square_feet = float(input('Enter the square feet: '))
	paint_price = float(input('Enter paint price per gallon: $'))
	calc(square_feet, paint_price)

def calc(square_feet, paint_price):
	gallons = square_feet / 115
	labor_hour = gallons * 8
	paint_charge = gallons * paint_price
	labor_charge = labor_hour * 20
	total = paint_charge + labor_charge
	print('The number of gallons of paint required: ', format(gallons, '.1f'))
	print('The hours of labor required: ', format(labor_hour, '.2f'))
	print('The cost of the paint: $', format(paint_charge, ',.2f'), sep='')
	print('The labor Charges: $', format(labor_charge, ',.2f'), sep='')
	print('Total cost of paint job: $', format(total, ',.2f'), sep='') 

main()
	
