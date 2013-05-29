# Program 6-2
# This program displays five random
# numbers in the range of 1 though 100.
import random

def main():
	for count in range(5):
		# Get a random number.
		number = random.randint(1, 100)
		print(number)

# Call the main function
main()
