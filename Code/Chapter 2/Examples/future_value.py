# Pseudocode
# Get the desired future value.
# Get the annual intrest rate.
# Get the number of years that the money will sit in the account.
# Calculate the amount that will have to be deposited
# Display the result of the calculation in step 4.

# Get the desired future value.
future_value = float(input('Enter the desired future value: '))

# Get the annual intrest rate.
rate = float(input('Enter the annual intrest rate: '))

# Get the number of years that the money will appreciate
years = int(input('Enter the number of years the money will grow: '))

# Calculate the amount needed to deposit.
present_value = future_value / (1.0 + rate)**years

# Display the amount needed to deposit.
print('You will need to deposit this amount:', present_value)
