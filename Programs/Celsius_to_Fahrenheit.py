"""
Author: Steven Pennington
Celsius_to_Fahrenheit v 1.0 last modified on 6/3/20
converts temprature from celsius to Fahrenheit

INPUT
	Temp in Celsius
	
Process
	Converte Celsius to Fahrenheit
	
OUTPUT
	Temp in Fahrenheit
"""

c = input("Enter digree celsius ")

f = (9/5)*float(c) +32

print(str("The temp in Fahrenheit is ") + str(f))

