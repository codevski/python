# Maximum of Two Values
# manimum_of_the_two.py
import math

def main():
	num1 = int(input('Enter first number: '))
	num2 = int(input('Enter second number: '))
	result = maximum(num1, num2)
	print(result)

def maximum(num1, num2):
	if num1 > num2:
		return num1
	else:
		return num2

main()
