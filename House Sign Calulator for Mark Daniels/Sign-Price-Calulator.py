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

def get_wood_type():
	print("Enter the Wood Type for your sign.")
	input_sign_wood_type = input("Oak '+$15' or Pine '+$0':")
	sign_wood_type = input_sign_wood_type.lower()
	if sign_wood_type in ['oak']:
		return 'Oak'
	elif sign_wood_type in ['pine']:
		return 'Pine'
	else:
		print("Error: Expected Oak or Pine, Got:" + input_sign_wood_type)
		time.sleep(2)
		clear_term()
		return -1

def GetOrder():
	order_num = input("Input order number:")
	cust_name = input("Input Customer Name:")
	wood_type = get_wood_type()
	while wood_type not in ['Oak','Pine']:
		wood_type = get_wood_type()
	print(order_num + wood_type)#debug line

#debuging code 

def debug():
	GetOrder()
debug()

#debuging code
