#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rock_paper_scissors.py
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
	x = random.randint(1, 3)
	if x == 1:
		x = 'ROCK'
	elif x == 2:
		x = 'PAPER'
	elif x == 3:
			x = 'SCISSORS'
	guess = input('rock, paper or scissors?: ')
	print('CPU: ', x, 'Player: ', guess)
	result = winner(x, guess)
	if result == 'tie':
		print('Its a tie try again!')
		main()
	else:
		print(result, 'Wins')
	
def winner(x, guess):
	if guess == 'scissors' and x == 'ROCK':
		win = 'rock'
		return win
	elif guess == 'paper' and x == 'SCISSORS':
		win = 'scissors'
		return win
	elif guess == 'paper' and x == 'ROCK':
		win = 'paper'
		return win
	elif guess == 'rock' and x == 'PAPER':
		win = 'paper'
		return win
	elif guess == 'rock' and x == 'SCISSORS':
		win = 'rock'
		return win
	else:
		win = 'tie'
		return win
if __name__ == '__main__':
	main()

