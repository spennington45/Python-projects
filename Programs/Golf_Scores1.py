"""
Author: Steven Pennington
Golf_Scores1 v 1.0 last modified on 6/10/20
Record names and golf scores in file golf.txt

INPUT
	Names
	Golf score
	
Process
	write to file golf.txt
	
OUTPUT
	None
"""

with open("golf.txt", "a") as f:
	name = input("Please enter name here.or type \"end\" when finished ")
	golfScore = input("Please enter golf score here. ")
	
	while name != "end":
		f.write(name + "\t" + golfScore + "\n")
		name = input("Please enter name here.or type \"end\" when finished ")
		if name != "end":
			golfScore = input("Please enter golf score here. ")

