def main():
	reclength1 = float(input('Enter Rectangle 1 Length: '))
	recwidth1 = float(input('Enter Rectabgle 1 Width: '))
	reclength2 = float(input('Enter Rectabgle 2 Width: '))
	recwidth2 = float(input('Enter Rectabgle 2 Width: '))
	calc(reclength1, recwidth1, reclength2, recwidth2)

def calc(recl1, recw1, recl2, recw2):

	rec1 = recl1 * recw1
	rec2 = recl2 * recw2

	if rec1 > rec2:
		print('Rectangle 1 has greater area')
	elif rec1 == rec2:
			print('They are the same')
	else:
		print('Rectangle 2 has a greater area')

main()
