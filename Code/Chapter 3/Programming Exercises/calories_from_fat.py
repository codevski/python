def main():
	fat_grams = float(input('Fat Grams: '))
	carb_grams = float(input('Carb Grams: '))
	calc(fat_grams, carb_grams)

def calc(fat, carb):
	calories_fat = fat * 9
	calories_carb = carb * 4
	print('Calories from fat is:', format(calories_fat, '.1f'))
	print('Calories from Carbs:', format(calories_carb, '.1f'))

main()
