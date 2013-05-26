# Programming Exercises
# Question 1 feet_to_inches.py
def main():
	inches, feet = feet_to_inches()
	print(feet,'feet converts to', inches,'inches') 

def feet_to_inches():
	feet = float(input('Enter Feet: '))
	inches = feet * 12
	return inches, feet

main()
