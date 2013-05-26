# Programming Exercises
# Question 8 Sum of Numbers

def main():
	num = float(input('Enter Number: '))
	total = 0.0

	while num >= 0:
		total += num
		num = float(input('Enter another number or negetive number to end: '))

	print('Total: ', format(total, ',.0f'), sep='')

main()
