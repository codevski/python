#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  random_guess_game.py
#  
#  Copyright 2013 techabyte <admin@techabyte.com.au>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import random

def main():
	keep_going = 'y'
	while keep_going == 'y':
		x = random.randint(1, 10)
		count = 1
		guess = int(input('Guess what the number is between 1 - 100: '))
		while guess != x:
			count += 1 
			if guess > x:
				print('High')
			else:
				print('Low')
			guess = int(input('Guess what the number is between 1 - 100: '))
		print('Congrats!, You guessed the correct number which was', x)
		print('You did a total of', count, 'guesses')
		print('Generating new random number')

main()
