# Programming Exercises
# Test Average and Grade

def main():
	for student in range(1):
		total = 0
		for tests in range(5):
			score = int(input('Enter Test Score: '))
			total += score
	avg = calc_average(total)
	grade = determine_grade(avg)
	print('Average: ', avg, 'Grade: ', grade)

def calc_average(total):
	avg = total / 5
	return avg

def determine_grade(avg):
	if avg >= 90:
		return 'A'
	elif avg >= 80:
		return 'B'
	elif avg >= 70:
		return 'C'
	elif avg >= 60:
		return 'D'
	elif avg <= 59:
		return 'F'

main()
