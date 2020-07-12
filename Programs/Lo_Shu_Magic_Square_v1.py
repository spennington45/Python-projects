"""
Author: Steven Pennington
Lo_Shu_Magic_Square v 1.0 last modified on 6/11/20
calculate the total rainfall and display statistics for varius facters

TEST LIST [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]
test list should be a Lo Shu Magic Square

INPUT
	2d list
	
Process
	Checks rows columns and diagonals for equality
	
OUTPUT
	Is this a Lo Shu Magic Square yes or no
"""


def main():
	
	i = 0
	j = 0
	k = 0
	list1 = []
	list2 = []
	list3 = []
	
	
	#square = [
	#    [4, 9, 2],
	#    [3, 5, 7],
	#    [8, 1, 6]
	#]
	print("[1, 2, 3]" + "\n" +
		"[4, 5, 6]" + "\n" +
		"[7, 8, 9]")


	while i < 3:
		list1.append(int(input("please provide input in the order shown in the example, i.e. 1 is where the first number input will go " )))
		i += 1

	while j < 3:
		list2.append(int(input("please provide input in the order shown in the example, i.e. 1 is where the first number input will go " )))
		j += 1

	while k < 3:
		list3.append(int(input("please provide input in the order shown in the example, i.e. 1 is where the first number input will go " )))
		k += 1

	square = [list1, list2, list3]
	t = sum(list3)
	
	if sum(list1) == t and sum(list1) == t and list1[0] + list2[0] + list3[0] == t and list1[1] + list2[1] + list3[1] == t and list1[2] + list2[2] + list3[2] == t and list1[0] + list2[1] + list3[2] == t and list1[2] + list2[1] + list3[0] == t:
		print("This is a Lo Shu Magic Square!!!!!")
	else: print("This is not a Lo Shu Magic Square.")


#	print(square)


main()
