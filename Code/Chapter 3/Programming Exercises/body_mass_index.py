def main():
	weight = float(input('Enter your weight in pounds:'))
	height = float(input('Enter your height in inches:'))
	bmi(weight, height)

def bmi(weight, height):
	bmi = weight * 703 / height**2
	print('Your Body Mass Index is: ', format(bmi, '.1f'))

main()
