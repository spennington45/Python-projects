"""
Author Steven Pennington
Population v 1.0 last modified on 6/7/20
Calculate the population over a given amount of time and growth rate for x number of starting organisms.

INPUT
	Starting population
	Growth rate in %
	Amount of time in days

PROCESSES
    Calculate the growth over time

OUTPUT
    Table of growth over time
            Day Approximate
            Population
"""


population = int(input("How many organisms in the inital population? "))
growthRate = int(input("What is the average growth rate of the organisms in a day (in %)? "))
days = int(input("How many days will the organisms be tracked? "))
i = 1
data = []
x = 0

while i <= days:
	data.append(str(i) + "\t")
	data.append(str(population) + "\n")
	i += 1
	population += population*growthRate/100

print("Day Approximate\tPopulation\n")

while x < days * 2:
        print(data[x] + "\t" + data[x + 1])
        x += 2
