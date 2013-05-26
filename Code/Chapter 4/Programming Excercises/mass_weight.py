MAX_WEIGHT = 1000
MIN_WEIGHT = 10

def main():
	mass = float(input("Enter Object's mass: "))
	calc(mass)

def calc(mass):
	weight = mass * 9.8

	if weight > MAX_WEIGHT:
		print('It is too heavy')
	elif weight < MIN_WEIGHT:
		print('Its too light')
	else:
		print('Its Fine')

main()
