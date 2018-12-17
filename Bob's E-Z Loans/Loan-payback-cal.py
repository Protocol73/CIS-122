#Python Bob's E-Z Loans
#For CIS122 p223 Q#9 
#By Protocol73
import os
import sys

try: #for py v2 vs v3 input
    input = raw_input
except NameError:
    pass

def clear_term(): #clear the Screen
    os.system('cls' if os.name=='nt' else 'clear')
    #...

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
	if Check_Prompt() is True:
		clear_term()
		sys.exit()
	else:
		print("Restarting Program")
		time.sleep(1)
		os.execl(sys.executable, sys.executable, *sys.argv)

#START
INTEREST = 0.01

clear_term()

def welcome_title():
	print("--- Bob's E-Z Loans---\n")

def get_input():
	global loan_amount,monthly_payment
	input_loan_amount = input("Loan Amount:")
	input_monthly_payment = input("Monthly Payment:")
	loan_amount = int(input_loan_amount)
	monthly_payment = int(input_monthly_payment)

def cal_payments():
	global loan_amount,monthly_payment
	print("Loan balance is:$" + str(loan_amount))
	while loan_amount > monthly_payment:
		loan_amount = loan_amount - monthly_payment
		loan_amount = loan_amount + (loan_amount * INTEREST)
		print("Loan Balance:$" +format(loan_amount,'.2f'))

def main():
	welcome_title()
	get_input()
	cal_payments()

main()