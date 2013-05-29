# Falling Distance
# falling_distance.py
import math

def main():
	for count in range(1, 10):
		dis = falling_distance(count)
		print(dis)

def falling_distance(count):
	d = (0.5) * (9.8) * (count**2)
	return d
main()
