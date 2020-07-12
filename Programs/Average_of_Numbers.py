"""
Author: Steven Pennington
Average_of_Numbers v 1.0 last modified on 6/10/20
takes a file called numbers.txt and finds the average

INPUT
	file numbers.txt or file input
	
Process
	Add files to a list
	Average the list
	
OUTPUT
	Print the average of the list
"""

def inputFile():
	f = input("File name or direcory? ")
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

	import statistics 
	list1 = []
	f = "numbers.txt"
	
	readFile = checkFile(f)
	
	for line in readFile:
		try:
			int(line)
		except:
			pass
		else:
			list1.append(int(line))
		
	avg = statistics.mean(list1)
	print(avg)
	readFile.close()
	
	
main()
	
