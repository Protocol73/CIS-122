# BLANK Python Script By Protocol73

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

#Program Functions

def startup():
	clear_term()
	print("Enter numbers to add,\n(Enter to input another number,0 to get total).")

def get_total():
	sum = 0
	addend = input("Addend:")
	while int(addend) is not 0:
		sum = int(addend) + sum
		addend = input("Addend:")
		continue
	print(sum)


def main():
	startup()
	get_total()

main()