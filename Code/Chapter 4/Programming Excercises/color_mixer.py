def main():
	color_1 = input('Enter a color (Red, Blue or Yellow): ')
	color_2 = input('Enter a color (Red, Blue or Yellow): ')
	mixer(color_1, color_2)

def mixer(color_1, color_2):
	if color_1 == 'blue' and color_2 == 'red':
		print('Purple')
	elif color_1 == 'red' and color_2 == 'yellow':
		print('Orange')
	elif color_1 == 'yellow' and color_2 == 'red':
		print('Orange')
	elif color_1 == 'blue' and color_2 == 'yellow':
		print('Green')
	elif color_1 == 'yellow' and color_2 == 'blue':
		print('Green')
	elif color_1 == 'red' and color_2 == 'blue':
		print('Purple')
	else:
		print('Invalid Color')

main()
