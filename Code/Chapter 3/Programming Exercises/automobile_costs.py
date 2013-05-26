# Main function ask user input
def main():
	loan_payment = float(input('Monthly cost for loan payments: $'))
	insurance = float(input('Monthly cost for insurance: $'))
	gas = float(input('Monthly cost for gas: $'))
	oil = float(input('Monthly cost for oil: $'))
	tires = float(input('Monthly cost for tires: $'))
	maintenance = float(input('Monthly cost for maintenance: $'))
	total_month(loan_payment, insurance, gas, oil, tires, maintenance)
	total_year(loan_payment, insurance, gas, oil, tires, maintenance)

# Monthly Calculations
def total_month(loan, insurance, gas, oil, tires, maintenance):
	monthly = loan + insurance + gas + oil + tires + maintenance
	print('Your Monthly Expenses: $', format(monthly, ',.2f'), sep='')

# Yearly Calculations
def total_year(loan, insurance, gas, oil, tires, maintenance):
	yearly = (loan + insurance + gas + oil + tires + maintenance) * 12
	print('Your Yearly Expenses: $', format(yearly, ',.2f'), sep='')

# Call the main function
main()

