#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  write_names.py
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
# This program gets three names from the user
# and writes them to a file.

def main():
	# Get three names.
	print('Enter the names of three friends.')
	name1 = input('Friend #1: ')
	name2 = input('Friend #2: ')
	name3 = input('Friend #3: ')
	
	# Open a file named friends.txt.
	myfile = open('friends.txt', 'w')
	
	# Write the names to the file.
	myfile.write(name1 + '\n')
	myfile.write(name2 + '\n')
	myfile.write(name3 + '\n')
	
	# Close the file
	myfile.close()
	print('The names were written to friends.txt')
	
# Call the main function
if __name__ == '__main__':
	main()

