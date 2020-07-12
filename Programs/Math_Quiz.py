"""
Author: Steven Pennington
Math_Quiz v 1.0 last modified on 6/9/20
Generate random addition math questions to be solved.

INPUT
	Answer
	
Process
	Generate random numbers
	Compare answer to corect answer
	
OUTPUT
	Give corect answer or congratulations
"""

import random

num1 = random.randint(1, 1000)
num2 = random.randint(1, 1000)

print("  ", num1, "\n", "+", num2)

answer = input("What is the answer? ")

if int(answer) == int(num1 + num2):
	print("Correct congratulations!")
else: print("The correct answer is " + str(num1 + num2))
