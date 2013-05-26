# User input total charge of meal
food_price = float(input('Price of the meal: $'))

# Calculate tip and tax
tip = food_price * 0.15
tax = food_price * 0.07
total = food_price + tip + tax

# Display each amount and total
print('Food Price: $', format(food_price, ',.2f'), sep='')
print('15% Tip: $', format(tip, ',.2f'), sep='')
print('Tax: $', format(tax, ',.2f'), sep='')
print('Total: $', format(total, ',.2f'), sep='') 
