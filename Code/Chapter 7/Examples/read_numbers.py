#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  read_numbers.py
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
# This program demostrates how numbers that are
# read from a file must be converted from strings
# before they are used in a math operation.

def main():
	# open a file for reading.
	infile = open('numbers.txt', 'r')
	
	# Read the three numbers from the file.
	num1 = int(infile.readline())
	num2 = int(infile.readline())
	num3 = int(infile.readline())
	
	# Close the file
	infile.close()
	
	# Add the three numbers.
	total = num1 + num2 + num3
	
	# Display the numbers and their total.
	print('The numbers are: ', num1, num2, num3)
	print('Their total is: ', total)

if __name__ == '__main__':
	main()

