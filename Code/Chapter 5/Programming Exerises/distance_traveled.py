# Programming Exercise 5
# Question 4

def main():
	total = 0.0
	speed = int(input('Enter Speed: '))
	time = int(input('Enter Hours: '))
	print('Hour\tDistance Traveled')
	print('--------------------------')
	
	for hours in range(1, time + 1):
		total = speed * hours
		print(hours, '\t', total)

main()
