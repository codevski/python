#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  file_write.py
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
# This program writes three lines of data
# to a file.

def main():
	# Open a file named philosophers.txt
	outfile = open('philosophers.txt', 'w')
	
	# Write the names of the three philosphers
	# ti this file
	outfile.write('John Locken\n')
	outfile.write('David Hume\n')
	outfile.write('Edmund Burke\n')
	
	# Close the file.
	outfile.close()

# Call the main function
if __name__ == '__main__':
	main()

