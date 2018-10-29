#For CIS122 p#224 Q10
#Written by Protocol73

import os
import sys
import time
import json

try: #for py v2 vs v3 input
    input = raw_input
except NameError:
    pass

def clear_term(): #clear the Screen
    os.system('cls' if os.name=='nt' else 'clear')
    #call to Clear the Terminal

def Check_Prompt():#For Asking the User Yes or No answers
	input_answer = input("Yes/No:")
	answer = input_answer.lower()
	if answer in ['n','no']:
		return False
	elif answer in ['y','yes']:
		return True
	else:
		print("Error: Expected Yes or No, Got:" + input_answer)
		time.sleep(2)
		clear_term()
		return -1

def end_of_job():#quits the Program
	print("Are you sure you want to quit?")
	print("No,Clears Data and Restarts the Kiosk.")
	if Check_Prompt() is True:
		clear_term()
		sys.exit()
	else:
		print("Restarting Program")
		time.sleep(1)
		os.execl(sys.executable, sys.executable, *sys.argv)

#START
clear_term()
rate = 1.05
TUITION = 10000

def welcome_screen():#<--
 	clear_term()
 	print("---Hunterville College Interest---")
 	

def math():
	print(TUITION)
	years = input("Years:")
	yr = int(years)
	for_year = TUITION
	print("\n---Interest for the next "+ years +" years---\n")
	
	while yr > 1:
		yr = yr - 1
		for_year = for_year * rate
		print(int(for_year))

	



def main():
	welcome_screen()
	math()
	print("\n")

main()