# -Protocol73
import os
import sys
def cls(): #clear the Screen
    os.system('cls' if os.name=='nt' else 'clear')
cls() 

HrsWorked = raw_input("Hours Worked:")
HrlyWage = raw_input("Hourly Wage:")

'''
if HrsWorked in ['q' or 'quit']:
     print("Goodbye")
     time.sleep(1)
     sys.exit()
'''

TAX_RATE = (0.20)
GrossWage =  int(HrsWorked) * float(HrlyWage)
TaxesOnEarned = GrossWage * TAX_RATE
earned = GrossWage -TaxesOnEarned

print("Yor Made: $" + str(earned))