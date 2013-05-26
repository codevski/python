# Global constants
BASE_HOURS = 40			# Base hours per week
OT_MULTIPLIER = 1.5		# Overtime multiplier

# The main function gets the number of hours worked and
# the hourly pay rate. It calls either the calc_pay_with_OT
# function or the calc_regular_pay function to calculate
# and display the gross pay.
def main():
	# Get the hours worked and the hourly pay rate.
	hours_worked = float(input('Enter the number of hours worked: '))
	pay_rate = float(input('Enter the hourly pay rate: '))

	# Calculate and display the gross pay.
	if hours_worked > BASE_HOURS:
		calc_pay_with_OT(hours_worked, pay_rate)
	else:
		calc_regular(hours_worked, pay_rate)

# The calc_pay_with_OT function calculates pay with
# overtime. It accepts the hours worked and the hourly
# pay rate as arguments. The gross pay is displayed.
def calc_pay_with_OT(hours, rate):
	# Calculate the number of overtime hours worked.
	overtime_hours = hours - BASE_HOURS

	# Calculate the amount of overtime pay
	overtime_pay = overtime_hours * rate * OT_MULTIPLIER

	# Calculate the gross pay.
	gross_pay = BASE_HOURS * rate + overtime_pay

	# Display the gross pay.
	print('The gross pay is: $', format(gross_pay, ',.2f'), sep='')

# The calc_regular_pay function calculates pay with
# no overtime. It accepts the hours worked and the hourly
# pay rate as arguments. The gross pay is displayed.
def calc_regular(hours, rate):
	# Calculate the gross
	gross_pay = hours * rate

	# Display the gross pay.
	print('The gross pay is: $', format(gross_pay, ',.2f'), sep='')

# Call the main function
main()
