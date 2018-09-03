#add&diff.py -Protocol73
import os
def clear_term(): #clear the Screen
    os.system('cls' if os.name=='nt' else 'clear')
clear_term() 

number1 = raw_input("Input a Number:")
number2 = raw_input("Put in another Number:")
added = int(number1) + int(number2)
diff = int(number1) - int(number2)

clear_term()
print ("Your Numbers added are:") + (str(added))
print ("And the Difference is:") + (str(abs(diff)))