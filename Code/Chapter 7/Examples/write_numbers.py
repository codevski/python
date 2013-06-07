#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  write_numbers.py
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
# This program demostrates how numbers
# must be converted to strings before they
# are written to a text file.

def main():
	# Open a file for writing.
	outfile = open('numbers.txt', 'w')
	
	# Get three numbers from the user.
	num1 = int(input('Enter a number: '))
	num2 = int(input('Enter a number: '))
	num3 = int(input('Enter a number: '))
	
	# Write the numbers to the file.
	outfile.write(str(num1) + '\n')
	outfile.write(str(num2) + '\n')
	outfile.write(str(num3) + '\n')
	
	# Close the file.
	outfile.close()
	print('Data written to numbers.txt')

# Call the main function.
if __name__ == '__main__':
	main()

