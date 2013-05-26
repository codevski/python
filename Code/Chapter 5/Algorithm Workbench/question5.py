# Algorithm Workbench
# Question 5

def main():
	total = 0.0

	for num in range(1, 31):
		total += num / (31 - num)
	print(total)
main()
