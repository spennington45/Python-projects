"""
Author: Steven Pennington
Capital_Quiz v 1.0 last modified on 6/17/20
Provide the user with a quiz of U.S. state capitals 

INPUT
	a capital
	
Process
	Check answer with dictionary
	
OUTPUT
	Tesult of quiz.
"""


capital_dic={
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'  }

import random
guess = ""
correct = 0
incorrect = 0

print("You will be prompted with the name of a state and be asked to type the name of the capital.  Remember \"Capitals\" and spelling matter, so the first letter in every word should be a capital letter.  When you are finished type \"quit\" and your score will be displayed.")

while guess != "quit":
	question = random.choice(list(capital_dic.keys()))
	guess = input("What is the capital of " + question + "? ")
	if guess == capital_dic[question] and guess != "quit":
		correct += 1
		print("Good job!")
	elif guess != "quit": 
		incorrect += 1
		print("Nice try but the correct answer is " + capital_dic[question])

print("You got " + str(correct) + " correct out of " + str(correct + incorrect) + ".")
	












