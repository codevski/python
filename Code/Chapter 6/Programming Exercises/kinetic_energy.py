# Programming Exercises
# Kinetic Energy
import math

def main():
	mass = int(input('Enter objects mass in kolograms: '))
	vel = int(input('Enter objects velocity in meters: '))
	ke = kinetic_energy(mass, vel)
	print('Objects Kinetics Energy is:', ke)

def kinetic_energy(mass, vel):
	ke = (0.5) * (mass) * (vel**2)
	return ke

main()
