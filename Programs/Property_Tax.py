"""
Author: Steven Pennington
Property_Tax v 1.0 last modified on 6/8/20
Calculates assessment value and property tax of land given the actual value.

INPUT
	Actual value
	
Process
	Calculate the assessment valuye
	Calculate the property tax
	
OUTPUT
	Assessment value
	Property tax
"""

actual = input("What is the actual valu of the property? ")

assessment = float(actual) * 0.6

propTax = float((assessment/100)*0.72)
round(propTax, 2)

print(f"Assessment value is ${assessment:.2f}")
print("Property tax is $ %.2f" % propTax)
