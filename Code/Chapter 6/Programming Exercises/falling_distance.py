# Falling Distance
# falling_distance.py
import math

def main():
	sec = int(input('falling time in secs: '))
	dis = falling_distance(sec)
	print(dis)

def falling_distance(sec):
	d = (0.5) * (9.8) * (sec**2)
	return d
main()
