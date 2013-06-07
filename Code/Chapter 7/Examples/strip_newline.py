#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  strip_newline.py
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
# This program reads the contents of the
# philosophers.txt file one line at a time.

def main():
	# Open a file named philosophers.txt
	infile = open('philosophers.txt', 'r')
	
	# Read the three lines from the file.
	line1 = infile.readline()
	line2 = infile.readline()
	line3 = infile.readline()
	
	# Strip the \n from each string.
	line1 = line1.rstrip('\n')
	line2 = line2.rstrip('\n')
	line3 = line3.rstrip('\n')
	
	# Close the file.
	infile.close()
	
	# Print the data that was read into memory.
	print(line1)
	print(line2)
	print(line3)

# Call the main function.
if __name__ == '__main__':
	main()

