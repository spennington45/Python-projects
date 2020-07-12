"""
Author: Steven Pennington
Area_of_Rectangles v 1.0 last modified on 6/3/20
Calculates the area of a rectangle

INPUT
	length
	width
	
Process
	length * width
	
OUTPUT
	area
"""

length = input("What is the length of the rectangle? ")
width = input("What is the width of the rectangle? ")

area = float(length) * float(width)

print("The area of the rectangle is " + str(area))
