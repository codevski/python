def main():
    days = int(input('Enter number of days: '))

    print('\nDay\t\tSalary')
    print('-----------------------')

    total_salary = 0.0

    for d in range(1, days + 1):
        salary = (2 ** (d - 1)) / 100
        total_salary += salary
        print(d, '\t\t', '$', format(salary, ',.2f'), sep='')
        
    print('\nTotal Pay: $', format(total_salary, ',.2f'), sep='')
main()
