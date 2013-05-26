# Programming Exercises 5
# Question 7 Pennies for Pay

def main():
	total = 0.0
	days = int(input('How many days?: '))

	print('Day\t\tSalary')
	print('-------------------------')

	for d in range(1, days + 1):
		pay = (2 ** (d - 1)) / 100
		total += pay
		print(d,'\t\t', '$', format(pay, ',.2f'), sep='')
	print('-------------------------')
	print('\tTotal: $', format(total, ',.2f'), sep='')

main()
