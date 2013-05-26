# Programming Excerise 5
# Question 5

def main():
	print('Celsious\tFahremheit')
	print('-----------------------')
	
	for c in range(0, 21):
		f = (9/5)*c + 32
		print(c,'\t\t', format(f, ',.1f'))

main()
