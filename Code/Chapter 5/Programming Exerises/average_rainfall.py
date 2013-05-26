# Programming Excersices 5
# Question 5 - Average Rainfall

def main():
	total = 0.0
	years = int(input('How mamy years?: '))

	for years in range(years):
		for months in range(1, 13):
			rain = float(input('How much rainfall for the month?: '))
			total += rain
			average = total / months

	print('Total Months:', months, 'Total Rainfall:', total, \
			'Average Rainfall:', format(average, ',.2f'))

main()
