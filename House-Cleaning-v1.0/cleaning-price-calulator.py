#Cleaning Bill Calulator
#Halzel's Housecleaning Service 
#Written By Protocol73 for Python 3.7

import os #for Clearing the Terminal
import sys #for sys.exit
import time #for time.sleep
from datetime import datetime #for Timestamps

print("Getting Ready") 

def clear_term(): #Clears the Terminal
    os.system('cls' if os.name=='nt' else 'clear')
clear_term() 

#Base Prices 

ServiceCallPrice = 40
BathroomPrice = 15
StandardRoomPrice = 10

#Defined strings

newline = ["\n"]
COMPANY_NAME = "Halzel's Housecleaning Service"

#for TimeStamps, Last name in Var is accuracy
Time_Now_Minute = datetime.now().strftime("%a, %B %d, %Y %I:%M")
Time_Now_Day = datetime.now().strftime("%a, %B %d, %Y")
Time_Now_Dash_Day = datetime.now().strftime("%m-%d-%y")

#Defined Logic & Checks

def math(): #do the Calulations for the total bill
	global totalBill
	totalBill = ServiceCallPrice + int(bathrooms) * BathroomPrice + int(standardRooms) * StandardRoomPrice
	pass

def BasePriceCheck(): #check that at least one room is included
	if totalBill <= 49:
		return False
	else:
		return True

def check_prompt():
	checked = input("y/n:")
	if checked in ['n','no']:
		return False
		check_prompt = False
	elif checked in ['y','yes']:
		return True
		pass

def info_check():
	clear_term()
	print("The Customer is:" + lastname)
	print("Is this Correct?")
	if check_prompt() is True:
		return True
	else:
		return False

def room_check():
	clear_term()
	print("There is: " + bathrooms + " Bathrooms" )
	print('And ' + standardRooms + ' Standard Rooms' )
	print("Is this Correct?")
	if check_prompt() is True:
		return True
	else:
		return False
	
#Defined Commands, calls, & Text

def end_of_job():#quits the Program
	print("Are you sure you want to quit?")
	if check_prompt() is True:
		clear_term()
		sys.exit()
		pass
	else:
		print("Restarting Program")
		time.sleep(1)
		os.execl(sys.executable, sys.executable, *sys.argv)

def user_quit_text():
	print("Enter ZZZZ to Quit")

#User input Functions

def customerLastname():
	global lastname
	lastname = input("Customers Last Name:")
	if lastname in ['zzzz','ZZZZ']:
		end_of_job()
	else:
		pass

def Num_of_bathrooms():
	clear_term()
	global bathrooms
	bathrooms = input("Number of Bathrooms:")
	if not bathrooms.isdigit():
		print("Must be a Whole Number")
		time.sleep(2)
		Num_of_bathrooms()
	else:
		pass

def Num_of_Standardrooms():
	global standardRooms
	standardRooms = input("Number of Standard Rooms:")
	if not standardRooms.isdigit():
		print("Must be a Whole Number")
		time.sleep(2)
		clear_term()
		Num_of_Standardrooms()
	else:
		pass

def get_num_rooms():#Get number of rooms from user
	Num_of_bathrooms()
	Num_of_Standardrooms()
	if room_check() is False:
		get_num_rooms()#to infinity & beyond!
	else:
		return True

def startup_text(): #Nice & clean start
	clear_term()
	print(COMPANY_NAME + " Bill Calulator")
	print("Today is: " + Time_Now_Day)

def startup_screen():#Start Main Screen
	startup_text()
	user_quit_text()
	customerLastname()

def receipt():
	banner = ("""------------------------------
Halzel's Housecleaning Service
------------------------------""")
	receiptFileName = lastname + "-" + Time_Now_Dash_Day + "-receipt.txt"
	fh = open(receiptFileName, "a")
	fh.writelines(banner)
	fh.writelines(newline)
	fh.writelines("Date: " + Time_Now_Day)
	fh.writelines(newline)
	fh.writelines("Receipt for:")
	fh.writelines(lastname.format())
	fh.writelines(" Household.")
	fh.writelines(newline)
	fh.writelines(newline)
	fh.writelines("Service Charge:$" + str(ServiceCallPrice))
	fh.writelines(newline)
	fh.writelines("+" + bathrooms + " Bathrooms at $" + str(BathroomPrice))
	fh.writelines(newline)
	fh.writelines("+" + standardRooms + " Standard Rooms at $" + str(StandardRoomPrice))
	fh.writelines(newline)
	fh.writelines(newline)
	fh.writelines("Total is: $" + str(totalBill))
	fh.writelines(newline)
	fh.writelines("Thank's for Choosing,")
	fh.writelines(newline)
	fh.writelines(banner)
	print("Saved Receipt as:",receiptFileName)
	time.sleep(3)
		
def main():
	while True is True:
		startup_screen()
		clear_term()
		if info_check() is False:
			main()
		else:
			pass
		if get_num_rooms() is True:
			pass
		math()
		if BasePriceCheck() is False:
			print("You must have at least one room.")
			time.sleep(2)
			get_num_rooms()
		else:
			print("The Total bill for the " + lastname, 'Family is $',totalBill)
			time.sleep(2)
		receipt()

main()