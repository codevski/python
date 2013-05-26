# Programming Exercises 5
# Question 9 Nested Loops

BASELINE = 1

for r in range(8, BASELINE, -1):
	for c in range(r - 1):
		print('*', end='')
	print()

