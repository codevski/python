# This program uses a loop to display a
# table of numbers and their squares.

def main():
	# Get the ending limit.
	print('This program displays a list of numbers')
	print('(starting at 1) and their squares.')
	end = int(input('How high should i go? '))

	# Print the table headings.
	print()
	print('Number\tSquares')
	print('---------------')

	# Print the numbers and their squares.
	for number in range(1, end + 1):
		square = number**2
		print(number, '\t', square)

# Call the main function
main()
