"""
Author: Steven Pennington
Calories_from_Fat_and_Carbohydrates v 1.0 last modified on 6/9/20
Calculate the number of caleries in food using the 4 9 4 rule. 

This question neglects proteins, which is another biological nutrent that can be used for energy. These calories, like carbohydrates can be estimated by multiplying the number of grams by 4 hence the 4 9 4 rule.   

INPUT
	Fat in grams
	carbohydrates in grams
	
Process
	Calculate sum of calories 
	
OUTPUT
	Calories
"""

carbGrams = int(input("How many carbs (in grams) are eaten per day? "))
fatGrams = int(input("How much fat (in grams) are eaten per day? "))
#proteinGrams = int(input("How much protein (in grams) are eaten per day? "))


calories = (carbGrams * 4) + (fatGrams * 9)# + (proteinGrams * 4)

print(str(calories) + " calories per day from fat and carbs")
