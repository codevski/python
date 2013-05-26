# Ask for price of 5 items
subtotal = float(input('Price of item: $'))
subtotal = subtotal + float(input('Price of item: $'))
subtotal = subtotal + float(input('Price of item: $'))
subtotal = subtotal + float(input('Price of item: $'))
subtotal = subtotal + float(input('Price of item: $'))

# Calculate Tax
sales_tax = subtotal * 0.06

# Display Total
print('The Subtotal is: $', format(subtotal, ',.2f'), sep='')
print('Total Tax: $', format(sales_tax, ',.2f'), sep='')
print('Total: $', format(subtotal + sales_tax, ',.2f'), sep='')
