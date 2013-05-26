# Algorithm Workbench
# Question 8
def main():
	num = int(input('Enter a number of 1 or above: '))

	while num < 1:
		print('The number you entered is bellow 1')
		num = int(input('Enter new number: '))
	print('YAY! The number you entered', num, 'is valid')
main()
