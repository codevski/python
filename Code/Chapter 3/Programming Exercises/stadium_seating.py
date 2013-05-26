def main():	
	class_a_sold = int(input('How many class a sold:'))
	class_b_sold = int(input('How many class b sold:'))
	class_c_sold = int(input('How many class c sold:'))
	calc(class_a_sold, class_b_sold, class_c_sold)

def calc(class_a, class_b, class_c):
	total = class_a * 15 + class_b * 12 + class_c * 9
	print('Total Income: $', format(total, ',.2f'), sep='')

main()
