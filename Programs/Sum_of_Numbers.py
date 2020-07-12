"""
Author Steven Pennington
Sum_of_Numbers v 1.0 last modified on 6/7/20
Calculate the sum of all positive numbers added.

INPUT
	Positive intigers 

PROCESSES
    sum all positive numbers

OUTPUT
    Sum of all postive numbers
"""

i = 0
list1 = []

print("Please add a positive number to the input unless you wish to stop adding, numbers then add a negative number")

while i >= 0:
	i = int(input("Input number here. "))
	if i >= 0:
		list1.append(i)
	else: print("") # had to add something here to fix EOS error but serves no purpose

print(list1)
print("Sum of numbers in above list is " + str(sum(list1)))
