# -Protocol73
import os
import sys
import time

def cls(): #clear the Screen
    os.system('cls' if os.name=='nt' else 'clear')
cls() 
print("Calulate your wages earned after 20% Taxes \nEnter a Negative Value to Quit.")
HrsWorked = raw_input("Hours Worked:")


#for number in HrsWorked:
if float(HrsWorked) < 1:
	cls()
	print ("Goodbye")
	time.sleep(2)
	cls()
	sys.exit()

HrlyWage = raw_input("Hourly Wage:")
TAX_RATE = (0.20)
GrossWage =  int(HrsWorked) * float(HrlyWage)
TaxesOnEarned = GrossWage * TAX_RATE
earned = GrossWage -TaxesOnEarned

print("You Made: $" + str(earned))