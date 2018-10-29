#For CIS122 p#224 Q12:a
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
def clear_ratings():
	global totalRatingsSaved,allTheStars,average_rating
	totalRatingsSaved = 0
	average_rating = 0
	allTheStars = 0

clear_term()
clear_ratings()

Theater = "Dubuque AMC"
Movie = "First Man"

def welcome_screen():#<--
 	clear_term()
 	print("---Hollywood Movie Rating Kiosk---")
 	print("--- at " + Theater + "---\n")

def userid_input():#User Scans Patron Card
	userid = input("Scan UserID or Patron Card:")
	if userid == str('073'):
		ManagerMenu()
	else:
		return userid 

def movie_to_rate():#print the Movie Name
	print("You are Rating: " + Movie + "\n")
	pass

def user_rating():#ask the user for there Rating
	global input_rating
	input_rating = 9
	print("Rate this movie on a scale of 0 to 4.")
	while input_rating not in ["0","1","2","3","4"]:
		input_rating = input("Your Rating:")
	else:
		print("\nRating Accepted\n\nThank You for Rating '",Movie,"'\nWe Hope to see you again soon.\n")#Would also print user Name based off UserID
		print("---" + Theater + " Theater ---\n")
		time.sleep(5)
		return True

def save_rating(rating):
	global allTheStars,totalRatingsSaved,average_rating
	allTheStars = allTheStars + int(rating)
	totalRatingsSaved = totalRatingsSaved + 1
	average_rating = allTheStars / totalRatingsSaved

def ManagerMenu():#
	clear_term()
	print('---Theater Employees Only---\n')
	print('[1] Print average rating for ',Movie)
	print('[2] Quit/Restart Kiosk (Will Clear Ratings for Movie:',Movie,')')
	print('[3] Run Kiosk')
	menu = input('Enter an option:')
	if int(menu) == (1):
		clear_term()
		print("The average rating for ",Movie,' is ',str(average_rating))
		input("Press Enter to continue...")
	elif int(menu) == (2):
		end_of_job()
	elif int(menu) == (3):
		run_kiosk()
	else:
		print("Error: Expected 1,2 or 3, Got:" + menu)
		time.sleep(2)
		clear_term()
	run_kiosk()

def main():
	welcome_screen()
	movie_to_rate()
	userid_input()
	if user_rating() is True:
		save_rating(input_rating)

def run_kiosk():
	while True:
		main()

run_kiosk()