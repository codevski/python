# Programming Excerises
# Prime Numbers

def main():
	num = int(input('Enter Number: '))
	result = is_prime(num)
	if result == True:
		print(num, 'is a prime number')
	else:
		print(num, 'not a prime number')

def is_prime(num):
	for x in range(2, int(num**0.5)+1):
		if num % x == 0:
			return False
	return True

main()
