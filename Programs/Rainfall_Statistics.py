"""
Author: Steven Pennington
Rainfall_Statistics v 1.0 last modified on 6/11/20
calculate the total rainfall and display statistics for varius facters

INPUT
	Rainfall for a given month
	
Process
	Add rainfall to a list
	Average and total of the list
	
OUTPUT
	Print the average total min and max of the list
"""

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December")
rainFall = []
x = 0
import statistics

while x < len(months):
	rainFall.append(int(input("Amount of rain (in inches) for the month " + months[x] + "? " )))
	x += 1
	

minRain = min(rainFall)
i = rainFall.index(minRain)
print("The lowest amount of rain was in " + months[i] + " and was " + str(minRain) + " inches")
maxRain = max(rainFall)
i = rainFall.index(maxRain)
print("The highest amount of rain was in " + months[i] + " and was " + str(maxRain) + " inches")
avg = statistics.mean(rainFall)
print("The average amount of rain for the year was " + str(avg) + " inches")
total = sum(rainFall)
print("The total amount of rain for the year was " + str(total) + " inches")

