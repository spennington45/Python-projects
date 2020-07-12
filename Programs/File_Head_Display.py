"""
Author: Steven Pennington
File_Head_Display v 1.0 last modified on 6/10/20
Display first 5 lines of a file

INPUT
	File name
	
Process
	Get first 5 lines
	
OUTPUT
	Print first 5 lines
"""

def inputFile():
	f = input("File name? ")
	return f

def checkFile(f):

	testFile = False
	
	while testFile == False:
		try:
			readFile = open(str(f), "r")
		except FileNotFoundError as e:
			print(e)
			f = inputFile()
			testFile = False
		except Exception as e:
			print(e)
		else: 
			testFile = True
			return readFile


def main():

	f = inputFile()
	
	readFile = checkFile(f)
	
	for line in range(5):
		print(readFile.readline(), end = "")
	readFile.close()


main()
	
