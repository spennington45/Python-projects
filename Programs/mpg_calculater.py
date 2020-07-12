"""
Author Steven Pennington
MPG(calculater v 1.0 last modified on 6/3/20
calculates miles per gallon (mpg)

INPUT
    Miles driven
    Gas used

PROCESSES
    devide miles driven by gas used

OUTPUT
    MPG
"""


milesDriven = input("Type number of miles driven ") 
gasUsed = input("Type gallons of gas used ")

mpg = float(milesDriven)/float(gasUsed)

print(str("Your vehicle has a mpg of ") + str(mpg))
