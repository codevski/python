def main():
	kilometers = float(input('Enter the Kilometer: '))
	km_to_miles(kilometers)

def km_to_miles(km):
	miles = km * 0.6214
	print(miles)
main()
