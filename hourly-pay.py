#Wage after Taxes -Protocol73 for CIS122
import os #for clear_term
import sys #for sys.exit()
import time # for time.sleep(#)

def clear_term(): #clear the Screen
    os.system('cls' if os.name=='nt' else 'clear')
clear_term() 

print("Calulate your wages earned after 20% Taxes \nEnter a Negative Value to Quit.")

HrsWorked = raw_input("Hours Worked:")

if float(HrsWorked) < 1:
	clear_term()
	print ("Goodbye")
	time.sleep(2)
	clear_term()
	sys.exit()

HrlyWage = raw_input("Hourly Wage:")
TAX_RATE = (0.20)
GrossWage =  int(HrsWorked) * float(HrlyWage)
TaxesOnEarned = GrossWage * TAX_RATE
earned = GrossWage - TaxesOnEarned

print("You Made: $" + str(earned))