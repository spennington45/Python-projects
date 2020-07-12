"""
Author: Steven Pennington
Age_Classifier v 1.0 last modified on 6/3/20
Classifies a person based on age into 3 catagories
	infant
	child
	Teenager
	adult

INPUT
	age
	
Process
	determin classification
	
OUTPUT
	classification
"""

age = input("Please inserte age here ")

if int(age) <= 1:
        classification = "infant"
elif int(age) < 13:
	classification = "child"
elif int(age) < 20:
	classification = "teenager"
else: classification = "adult"

print(classification)
