# This program uses a loop to display a
# table showing the numbers 1 through 10
# and their squares.

def main():
	# Print the table headings.
	print('Number\tSquares')
	print('---------------')

	# Print the numbers 1 through 10
	# and their squares.
	for number in range(1, 11):
		square = number**2
		print(number, '\t', square)

# Call the main function
main()
