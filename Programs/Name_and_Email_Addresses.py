"""
Author: Steven Pennington
Name_and_Email_Addresses v 1.0 last modified on 6/17/20
Keep and manage a dictionary of contacts

INPUT
	Pick from a menu and give appropriat imput for selection
	
Process
	preform selected task to manage the list of contacts
	
OUTPUT
	appended file
"""

# Used to look up a contact's email
def lookUp(contact_list):
	name = input("Who would you like to look up? ")
	if name in contact_list:
		print("Email address is: " + contact_list[name])
	else:
		print(name + " is not a contact") 

# Used to add a contact to the dictionary contact_list
def addContact(contact_list):
	newContact = input("Enter the name of the contact. ")
	if newContact != "6" and newContact != "quit":
		newEmail = input("Enter the email of the contact. ")
		contact_list[newContact] = newEmail
	return contact_list
	
# Used to change an email in an existing contact 
def changeContact(contact_list):
	key = input("Who's email would you like to change? ")
	while key not in contact_list:
		if key == "6" or key == "quit":
			break
		else:
			print(key + " is not a contact")
			key = input("Who's email would you like to change? ")
	if key in contact_list:
		newEmail = input("What is thair new email? ")
		contact_list[key] = newEmail
	return contact_list

# used to delete an email from the contact_list dictionary
def deleteContact(contact_list):
	deleteName = input("Who would you like to delete? ")
	while deleteName not in contact_list:
		if deleteName == "6" or deleteName == "quit":
			break
		else:
			print(deleteName + " is not a contact")
			deleteName = input("Who would you like to delete? ")
	if deleteName in contact_list:
		del contact_list[deleteName]
	return contact_list

# Displays the menu of choices for the user to pick from.
def display(choice):
	print("You may leave a menu at any point by typing quit or 6 \n Please chuse a numbered option from the following list. \n 1) Look up a contact \n 2) Add a contact \n 3) Change a contact \n 4) Deleate a contact \n 5) To see all contacts \n 6) To quit")
	try:
		choice = int(input("What would you like to do? "))
	except:
		pass
	else:
		if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6:
			return choice
		else:
			print("Invalid choice please pick again.")
			return choice

def main():
	
	import pickle
	import os
	
	choice = ""
	
	#Tests if the file exists and if not creates it and makes the var contact_list otherwise sets contact_list = to what is in the file.
	try:
		if os.stat("contact_list.txt").st_size < 10:
			f = open("contact_list.txt", "wb")
			contact_list = {}
			f.close()
		else: 
			f = open("contact_list.txt", "rb")
			contact_list = pickle.load(f)
			f.close()
	except FileNotFoundError:
		f = open("contact_list.txt", "wb")
		contact_list = {}
		pickle.dump(contact_list, f)
		f.close()
	except Exception:  
		f = open("contact_list.txt", "rb")
		contact_list = pickle.load(f)
		f.close()

	f = open("contact_list.txt", "wb")
	
	while choice != 6:
		choice = display(choice)
		if choice == 1:
			lookUp(contact_list)
		if choice == 2:
			contact_list = addContact(contact_list)
		if choice == 3:
			contact_list = changeContact(contact_list)
		if choice == 4:
			contact_list = deleteContact(contact_list)
		if choice == 5:
			print(contact_list)
		
	
	
	pickle.dump(contact_list, f)
	
	
	f.close()
	
main()
