"""
Author Steven Pennington
Bug_Collector v 1.0 last modified on 6/7/20
Calculate the total number of bugs collected in a given timeframe

INPUT
	Bugs collected

PROCESSES
    sum all bugs collected

OUTPUT
    Total number of bugs collected
"""

day = 1
total = 0

while day <= 5: # number of days can be modified as needed for differing timeframes.
        total += int(input("How many bugs were collected today? "))
        day += 1
	
print(str(total) + " bugs collected over " + str(day - 1) + " days.")
