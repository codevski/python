# This program assists a technician in the process
# of checking a substance's temperature.

# MAX_TEMP is used as a global constant for
# the maximum temperature.
MAX_TEMP = 102.5

# The main function
def main():
	# Get the substance's temperature.
	temperature = float(input("Enter the substance's Celsius temperature: "))

	# As long as necessary, instruct the user to
	# adjust the thermostat.
	while temperature > MAX_TEMP:
		print('The termperature is too high.')
		print('Turn the thermostat down and wait')
		print('5 minutes. Then take the termperature')
		print('again and enter it.')
		temperature = float(input('Enter the new Celsius temperature: '))

	# Remind the user to check the temperature again
	# in 15 mins.
	print('The temperature is acceptable.')
	print('Check it again in 15 minutes.')

# Call the main function
main()
