PERCENT = 0.80

def main():
	replacement_cost = float(input('Enter the replacement cost: $'))
	calc(replacement_cost)

def calc(rep_cost):
	insurance = rep_cost * PERCENT
	print('Insurance will cover: $', format(insurance, ',.2f'), sep='')

main()
