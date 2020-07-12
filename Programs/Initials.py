"""
Author: Steven Pennington
Initials v 1.0 last modified on 6/16/20
Prints out initials of name entered

INPUT
	Name
	
Process
	Get the first letter of the name
	
OUTPUT
	Initials
"""

firstName = input("What is your first name? ").upper()
middleName = input("What is your middle name? ").upper()
lastName = input("What is your last name? ").upper()


print(firstName[0] + ". " + middleName[0] + ". " + lastName[0])
