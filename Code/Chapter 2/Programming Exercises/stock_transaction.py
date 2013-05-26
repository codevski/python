# Calculations
buy_stock = 32.87 * 1000
com_buy = buy_stock * 0.02
sell_stock = 33.92 * 1000
com_sell = sell_stock * 0.02
profit = sell_stock - com_sell - buy_stock - com_buy

# Display Results
print('Amount paid stock Total: $', format(buy_stock, ',.2f'), sep='')
print('Buy Commission: $', format(com_buy, ',.2f'), sep='')
print('Sold Stock Total: $', format(sell_stock, ',.2f'), sep='')
print('Sell Commission: $', format(com_sell, ',.2f'), sep='')
print('Profit: $', format(profit, ',.2f'), " Note: If negative its a loss", sep='')
