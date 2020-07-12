"""
Author: Steven Pennington
Lo_Shu_Magic_Square v 2.0 last modified on 6/14/20
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
# Calculate the sum of nested elements in square
def sumListElem(elem): 
	x = 0
	for i in (elem):
		x += int(i)
	return x

# Test for duplicate values in square
def testLength(square, goodSquare):
	test = []
	testExcept = ""
	try:
		for i in square:
			for j in i:
				test.append(int(j))
		testExcept = max(test)
	except Exception:
		print("Only intagers will be accepted")
		return False
	else:
		if len(test) == len(set(test)) and int(max(test)) < int(10) and int(min(test) > 0):
			goodSquare = True
			return True
		else:
			print("Invalid input no duplicates allowed and value should be 1-9.")
			print("The highest value entered is " + str(max(test)))
			print("The lowest value entered is "+ str(min(test)))
			goodSquare = False
			return False

# Get input from the user and place it in a 3x3 nested list, see TEST LIST above for example.
def LSMSinput(square):
	tepm = []
	for first in range(3):
		temp = []
		for second in range(3):
			temp.append(input('Enter a Magic number from the sequence'))
		square.append(temp)
	return square


def main():

	
	#square = [
	#    [4, 9, 2],
	#    [3, 5, 7],
	#    [8, 1, 6]
	#]
	print("Enter values for a Lo Shu Magic Square where the number are entered in the order of the example below. i.e. first number entered will appear where the 1 is and the second number entered will appear where the 2 is and so on.")
	print("[1, 2, 3]" + "\n" +
		"[4, 5, 6]" + "\n" +
		"[7, 8, 9]")

	tepm = []
	square = []
	goodSquare = False
	
	LSMSinput(square)
	
	while goodSquare == False:
		if testLength(square, goodSquare) == False:
			square = []
			LSMSinput(square)
		else: break

	
	print(str(square[0]) + "\n" + str(square[1]) + "\n" + str(square[2]))
	t = sumListElem(square[0])
	

	if sumListElem(square[1]) == t and sumListElem(square[2]) == t and int(square[0][0]) + int(square[1][0]) + int(square[2][0]) == t and int(square[0][1]) + int(square[1][1]) + int(square[2][1]) == t and int(square[0][2]) + int(square[1][2]) + int(square[2][2]) == t and int(square[0][0]) + int(square[1][1]) + int(square[2][2]) == t and int(square[0][2]) + int(square[1][1]) + int(square[2][0]) == t:
		print("This is a Lo Shu Magic Square!!!!!")
	else: print("This is not a Lo Shu Magic Square.")




main()
