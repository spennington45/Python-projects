"""
Author: Steven Pennington
Magic_8_Ball v 1.0 last modified on 6/11/20
Simulates a magic 8 ball toy

INPUT
	A string in the form of a yes or no question
	
Process
	Generate a random responce
	
OUTPUT
	Print the responce
"""

def main():
	
	answer = []
	import random
	question = ""
	
	with open("8_ball_responses.txt", "r") as f:
		for line in f:
			answer.append(line)
			

	print("Type \"quit\" when you are finished.")
	
	while question != "quit":
		question = str(input("What is your question? "))
		if question != "quit":
			i = random.randint(0,11)
			print(answer[i])
		
	
	
	
	
main()
