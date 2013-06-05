#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  future_value.py
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
	current_value = float(input('Enter Current Value: $'))
	interest = float(input('Enter monthly interest rate: $'))
	months = float(input('How many months: '))
	future_value = calc(current_value, interest, months)
	print('Your future value: $', format(future_value, ',.2f'), sep='')

def calc(cv, rate, months):
	future = cv * (1 + rate)**months
	return future

main()
