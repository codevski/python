#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  write_sales.py
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
# This program prompts the user for sales amounts
# and writes those amounts to the sales.txt file.

def main():
	# Get the number of days.
	num_days = int(input('For how many days do ' + \
						'you have sales? '))
						
	# Open a new file named sales.txt.
	sales_file = open('sales.txt', 'w')
	
	# Get the amount of sales for each day and write
	# it to the file.
	for count in range(1, num_days + 1):
		# Get the sales for a day.
		sales = float(input('Enter the sales for day #' + \
							str(count) + ': '))
		
		# Write the sales amount to the file.
		sales_file.write(str(sales) + '\n')
	
	# Close the file.
	sales_file.close()
	print('Data written to sales.txt')

# Call the main function
if __name__ == '__main__':
	main()

