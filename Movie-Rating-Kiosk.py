#For CIS122 p#224 Q12:a
#Written by Protocol73

import os
import sys
import time

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
	if Check_Prompt() is True:
		clear_term()
		sys.exit()
	else:
		print("Restarting Program")
		time.sleep(1)
		os.execl(sys.executable, sys.executable, *sys.argv)

#START
clear_term()

Theater = "DBQ Mall"
MOVIE = "ANT-MAN"

def welcome_screen():
 	clear_term()
 	print("---Hollywood Movie Rating Kiosk---")
 	print("--- at " + Theater + "\n")

def movie_to_rate():#print the Movie Name
	print("You are Rating:" + MOVIE + "\n")
	pass

def user_rating():#ask the user for there Rating
	input_rating = 9
	print("Rate this movie on a scale of 0 to 4.")
	while input_rating not in ["0","1","2","3","4"]:
		input_rating = input("Your Rating:")
		if int(input_rating) < 0:
			end_of_job()
		else:
			pass	
	else:
		print("Valid Rating")

def userid_input():
	userid = input("UserID #:")		

def main():
	welcome_screen()
	movie_to_rate()
	userid_input()
	user_rating()
while True:
	main()