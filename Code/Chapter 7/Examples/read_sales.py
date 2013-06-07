#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  read_sales.py
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
# This program reads all of the values in
# the sales.txt file.

def main():
	# Open the sales.txt file for reading.
	sales_file = open('sales.txt', 'r')
	
	# Read the first line from the file, but
	# don't convert to a number yet. We still
	# need to test for an empy string.
	line = sales_file.readline()
	
	# As long as an empty string is not returned
	# from readline, continue processing
	while line != '':
		# Convert line to a float
		amount = float(line)
		
		# Format and display the amount.
		print(format(amount, '.2f'))
		
		# Read the next line
		line = sales_file.readline()
		
	# Close the file.
	sales_file.close()

# Call the main function.
if __name__ == '__main__':
	main()

