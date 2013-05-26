# This program displays a stair-step pattern.
NUM_STEPS = 6

for r in range(NUM_STEPS):
	for c in range(r):
		print(' ', end='')
	print('#')
