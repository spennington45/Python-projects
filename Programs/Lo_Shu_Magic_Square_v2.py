"""
Author: Steven Pennington
Lo_Shu_Magic_Square v 2.0 last modified on 6/13/20
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
def sumListElem(elem):
	x = 0
	for i in (elem):
		x += int(i)
	return x

def main():

	
	#square = [
	#    [4, 9, 2],
	#    [3, 5, 7],
	#    [8, 1, 6]
	#]
	print("[1, 2, 3]" + "\n" +
		"[4, 5, 6]" + "\n" +
		"[7, 8, 9]")

	tepm = []
	square = []
	
	for first in range(3):
		temp = []
		for second in range(3):
			temp.append(input('Enter a Magic number from the sequence'))
		square.append(temp)
	
	t = sumListElem(square[0])
	

	if sumListElem(square[1]) == t and sumListElem(square[2]) == t and int(square[0][0]) + int(square[1][0]) + int(square[2][0]) == t and int(square[0][1]) + int(square[1][1]) + int(square[2][1]) == t and int(square[0][2]) + int(square[1][2]) + int(square[2][2]) == t and int(square[0][0]) + int(square[1][1]) + int(square[2][2]) == t and int(square[0][2]) + int(square[1][1]) + int(square[2][0]) == t:
		print("This is a Lo Shu Magic Square!!!!!")
	else: print("This is not a Lo Shu Magic Square.")


#	print(square)


main()
