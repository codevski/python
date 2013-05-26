def main():
	number = int(input('Enter a number between 1 to 10: '))
	romain(number)
	

def romain(num):
	if num == 1:
		print('I')
	elif num == 2:
		print('II')
	elif num == 3:
		print('III')
	elif num == 4:
		print('IV')
	elif num == 5:
		print('V')
	elif num == 6:
		print('VI')
	elif num == 7:
		print('VII')
	elif num == 8:
		print('VIII')
	elif num == 9:
		print('IX')
	elif num == 10:
		print('X')
	else:
		print('Number is not between 1 - 10')

main()
