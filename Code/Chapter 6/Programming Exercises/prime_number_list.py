#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prime_number_list.py
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

def main():
	for number in range(101):
		prime = is_prime(number)
		if prime == True:
			print(number)
		
def is_prime(num):
	for x in range(2, int(num**0.5)+1):
		if num % x == 0:
			return False
	return True
main()
