"""
Author: Steven Pennington
Sentence_Capitalizer v 1.0 last modified on 6/16/20
capitaliz the first charicter in a sentence. 

INPUT
	a string
	
Process
	capitaliz the first charicter in a sentence. 
	
OUTPUT
	the string with capitalized first words of sentences
"""

UPPERCASE = {   'a':'A', 'b':'B', " ":" ",
                'c':'C', 'd':'D', 'e':'E', 
                'f':'F', 'g':'G', 'h':'H', 
                'i':'I', 'j':'J', 'k':'K', 
                'l':'L', 'm':'M', 'n':'N', 
                'o':'O', 'p':'P', 'q':'Q', 
                'r':'R', 's':'S', 't':'T', 
                'u':'U', 'v':'V', 'w':'W', 
                'x':'X', 'y':'Y', 'z':'Z'}

newSentence = ""
i = 1
sentence = input("Type a sentence here: ")

try:
	newSentence += UPPERCASE[sentence[0]]
except:
	newSentence += sentence[0]

while  i < len(sentence):
	if newSentence[i-2] == "." or newSentence[i-2] == "?" or newSentence[i-2] == "!":
		newSentence += UPPERCASE[sentence[i]]
		i += 1
	else: 
		newSentence += sentence[i]
		i += 1


print(newSentence)
