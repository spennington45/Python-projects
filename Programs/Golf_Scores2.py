"""
Author: Steven Pennington
Golf_Scores2 v 1.0 last modified on 6/10/20
Reads and displays golf.txt

INPUT
	None
	
Process
	Read golf.txt
	
OUTPUT
	Context of golf.txt with a header
"""

with open("golf.txt", "r") as f:
	print("Name" + "\t" + "Golf Score")
	print("--------------------")
	print(f.read())
