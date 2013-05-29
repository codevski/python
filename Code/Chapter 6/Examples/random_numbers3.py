# Program 6-3
# This porgram displays five random
# numbers in the range of 1 though 100.
import random

def main():
	for count in range(5):
		print(random.randint(1, 100))

# Call main function
main()
