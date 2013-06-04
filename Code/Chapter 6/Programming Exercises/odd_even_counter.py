# Programming Excercises
# Odd/Even Counter
import random

def main():
	print('Now generating 100 random numbers \nCalculating ' \
			'how many of them are odd and even..........')
	for count in range(1):
		even = 0
		odd = 0
		for count in range(100):
			number = random.randint(1, 100)
			if number % 2 == 0:
				even += 1
			else:
				odd += 1
	print('Even:', even, 'Odd:', odd)

main()
