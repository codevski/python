# Ask the user to enter total square feet
square_feet = float(input('Enter the total of square feet: '))

# Divide the amount entered by 43,560 to get the
# number of acres
acres = square_feet / 43560

# Display the results
print('You have a total of ', format(acres, '.1f'), 'acres')
