"""
Author: Steven Pennington
Body_Mass_Index v 1.0 last modified on 6/3/20
Calculates someone's BMI

INPUT
	Weight
	Height
	
Process
	Calculate BMI
	
OUTPUT
	BMI
	Optimal BMI
"""

weight = input("Enter weight in lbs ")
height = input("Enter hight in inches ")

bmi = float(weight)*703/(int(height)**2)

if bmi < 18.5:
	opt = "underweight" #opt = optimal BMI status
elif bmi <= 25:
	opt = "optimal"
else: opt = "overweight"

print("BMI = " + str(bmi) + " " + opt)

