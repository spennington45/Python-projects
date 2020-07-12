"""
Author: Steven Pennington
Mounthly_Sales_Tax v 1.0 last modified on 6/9/20
Calculates the amount of county, state and total sales tax for a given month.

INPUT
	Total sails for the month
	
Process
	Calculate the county sails tax
	Calculate the state sails tax
	Calculate the total sails tax
	
OUTPUT
	county sails tax
	state sails tax
	total sails tax
"""

sails = float(input("What is the total in sails for this month? "))

countyTax = sails * 0.025
stateTax = sails * 0.05
totalTax = countyTax + stateTax

print("The amount of county sails tax $%.2f" % countyTax)
print("The amount of state sails tax $%.2f" % stateTax)
print("The total sales tax $%.2f" % totalTax)
