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
