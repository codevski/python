# Ask user miles driven
miles_driven = float(input('Miles Driven: '))

# Ask user gas used
gas_used = float(input('Gas Used: '))

# Calculate how much gallon used per mile
mpg = miles_driven / gas_used

# Display MPG
print(format(mpg, ',.1f'), 'Miles-Per-Gallon')
