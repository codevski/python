# Programming Exercises
# Question 2
def main():
	CAL = 3.9
	total = 0.0
	print('If you burn 3.9 calories per min:')
	for mins in range(10, 31, 5):
		total += mins * CAL
		print('For', mins,'mintues you burn', total, 'calories!')
main()
