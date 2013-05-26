# Ask user of amount of purchase
subtotal = float(input('Purchase amount: $'))

# Tax Calculation
state_sales_tax = subtotal * 0.04
county_tax = subtotal * 0.02

# Display amount
print('Subtotal: $', format(subtotal, ',.2f'), sep='')
print('State Tax: $', format(state_sales_tax, ',.2f'), sep='')
print('County Tax: $', format(county_tax, ',.2f'), sep='')
print('Total: $', format(subtotal + state_sales_tax + county_tax, ',.2f'), sep='')
