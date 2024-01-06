"""
Put the functions for the example printing_models.py in a separate file called printing_functions.py
Call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""

#Defining the functions to import them on printing_models.py

def printing_designs(unprinted, completed):
	while unprinted:
		current = unprinted.pop()
		print(f"Printing model: {current.title()}")
		completed.append(current)

def show_printed_designs(completed):
	print("\nThe completed designs are : ")
	for i in completed: 
		print(f'- {i.title()}')