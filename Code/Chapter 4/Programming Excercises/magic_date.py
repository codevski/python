def main():
	month = int(input('Enter month, eg 04 for April: '))
	day = int(input('Enter date: '))
	year = int(input('Enter Year two digit only, eg 10 for 2010: '))

	magic = month * day

	if year == magic:
		print('The date is magic')
	else:
		print('The date is not magic')

main()
