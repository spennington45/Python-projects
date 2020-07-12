"""
Author: Steven Pennington
Shipping_Charges v 1.0 last modified on 6/3/20
Calculates the cost of shipping for a given weight of package

INPUT
	Weight of package
	
Process
	Calculate cost of shipping
	
OUTPUT
	cost of shipping in USD
"""

weight = input("Weight of package (in lbs) to be shipped? ")
cost = "$0.00"

if float(weight) <= 2:
	cost = "$1.50"
elif float(weight) <= 6:
	cost = "$3.00"
elif float(weight) <= 10:
	cost = "$4.00"
else: cost = "$4.75"

print("The cost is " + cost)
