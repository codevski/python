# Programming Exercises
# Question 1 Bug Collector

def main():
	total = 0

	for days in range(1, 8):
		print('Day', days)
		bugs = int(input('How many bugs today: '))
		total += bugs
	print('You have collected', total, 'bugs!')
main()
