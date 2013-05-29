# Falling Distance
# falling_distance.py
import math

def main():
	for count in range(1, 11):
		dis = falling_distance(count)
		print('The falling distance is ', format(dis, ',.2f'), 'M', sep='')

def falling_distance(count):
	d = (0.5) * (9.8) * (count**2)
	return d
main()
