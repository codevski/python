#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  file_read.py
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
# This program reads and displays the contents
# of the philosophers.txt file.

def main():
	# Open a file named philosophers.txt.
	infile = open('philosophers.txt', 'r')
	
	# Read the files contents.
	file_contents = infile.read()
	
	# Close the file.
	infile.close()
	
	# Print the data that was read into memory
	print(file_contents)

# Call the main function
if __name__ == '__main__':
	main()

