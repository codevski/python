# Algorithm Workbench
# Question 9

def main():
	num = int(input('Enter a number between 1 to 100: '))

	while num < 1 or num > 100:
		print('Dude You fucked it, I said number between 1 to 100')
		num = int(input('Lets try again: '))

	print('Nice you can count')
main()
