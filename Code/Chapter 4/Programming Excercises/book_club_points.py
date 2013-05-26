def main():
	books = int(input('Enter amount of books purchased this month: '))
	calc(books)

def calc(books):
	if books >= 4:
		print('60 points')
	elif books >= 3:
		print('30 points')
	elif books >= 2:
		print('15 points')
	elif books >= 1:
		print('5 points')
	else:
		print('No Points')

main()
