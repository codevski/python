# Programming Exercises 5
# Question 3

def main():
	budget = float(input('Enter your budget: $'))
	exp = float(input('Enter your Expense or enter 0 to end: $'))
	total = 0.0

	while exp != 0:
		total += exp
		exp = float(input('Another Expense: $'))

	difference = total - budget

	if total > budget:
		print('You have spent $', format(total, ',.2f'), 'Your over your budget by $', format(difference, ',.2f'), sep='')
	elif total < budget:
		print('You have spent $', format(total, ',.2f'), ' Your under your budget by $', format(difference * -1, ',.2f'), sep='')
main()
