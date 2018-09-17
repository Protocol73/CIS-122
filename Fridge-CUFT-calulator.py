#Arnie's Fridge  CU FT calulator
import os

def clear_term(): #Clears the Terminal
    os.system('cls' if os.name=='nt' else 'clear')
clear_term() 

print("Arnie's Fridge CU.FT calulator.")

model_num = input("Enter Fridge Model Number:")

height = input("Enter internal height of Fridge:")

width = input("Enter internal width of Fridge:")

depth = input("Enter internal depth of Fridge:")

clear_term() 

cuft =  