# Sign-Price-Calulator Script By Protocol73
#For Chapter 4 p.173

import os 
import sys 
import time

try: #for py v2 vs v3 input
    input = raw_input
except NameError:
    pass

def clear_term(): #clear the screen
    os.system('cls' if os.name=='nt' else 'clear')
    #I like the terminal nice & clean

def check_prompt():#For Asking Yes or No Questions
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

#Static Prices

SIGN_MINIMUM_PRICE = 30
SIGN_OAK_WOOD_PRICE = 15

CHARACTERS_EXTRA = 3
CHARACTERS_GOLD_LEAF = 12


#Program Functions

def welcome_text():
	print("------------------------------")
	print("Mark Daniels Carpentry & Signs\nSign Price Calulator")
	print("------------------------------")

def ProgramModeTitle(mode):
	clear_term()
	if mode == 'a':
		print("Mode 1: Saving all correct data entered")
	elif mode == 'b':
		print("Mode 2: Only showing data for Oak signs w/ five characters")
	elif mode == 'c':
		print("Mode 3: Only Showing Data From Signs w/\nPine Wood, Gold Lettering and 10+ Characters")
	else:
		return False

def SetProgramMode():
	input_mode = input("Set Program Data Saving Mode. A,B or C.\nMode:")
	mode = input_mode.lower()
	ProgramModeTitle(mode)
	if ProgramModeTitle(mode) is False:
		return -1
	return mode

def get_wood_type():
	print("Enter the Wood Type for your sign.")
	input_wood_type = input("Oak '+$15' or Pine '+$0':")
	wood_type = input_sign_wood_type.lower()
	if wood_type in ['oak']:
		return 'Oak'
	elif wood_type in ['pine']:
		return 'Pine'
	else:
		print("\nError: Expected Oak or Pine, Got:" + input_sign_wood_type + "\n")
		return -1

def GetOrderInfo():
	global sign_wood_type,order_num,cust_name
	order_num = input("Input order number:")
	if order_num in ['changemode']:
		return 9
	cust_name = input("Input Customer Name:")
	if cust_name in ['changemode']:
		return 9
	sign_wood_type = get_wood_type()
	while wood_type not in ['Oak','Pine']:
		wood_type = get_wood_type()
	
	print(order_num + wood_type)#debuging line -------------------------- REMOVE


def sign_price_cal():
	price_math = SIGN_MINIMUM_PRICE
	if sign_wood_type is 'Oak':
		price_math = price_math + SIGN_OAK_WOOD_PRICE
	else:
		pass
	#if :
		#price_math =   


	return sign_price_total

def mode_running(mode):
	welcome_text()
	if mode == 'a':
		#do a mode stuff
	elif mode == 'b':
		#do b mode stuff
	elif mode == 'c':
		#do a mode stuff




#debug code -------------------------- REMOVE

def debug():
	clear_term()
	current_mode = SetProgramMode()
	mode_running(current_mode)

debug()

#debug code -------------------------- REMOVE
