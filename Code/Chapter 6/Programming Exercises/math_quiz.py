# Programming Exercises 6
# Question 2
# Math Quiz
import random

def main():
	total = calc()
	answer = int(input('Answer is: '))
	if answer == total:
		print('Correct')
	else:
		print('Incorrect, The correct answer is', total)

def calc():
	num1 = random.randint(1, 10)
	num2 = random.randint(1, 10)
	print(num1,'+', num2)
	return num1 + num2
main()
