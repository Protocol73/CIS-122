#Python Bob's E-Z Loans
#For CIS122 p223 #9 
#By Protocol73

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
clear_term()

def welcome_title():
	print("--- Bob's E-Z Loans---\n")

def get_input():
	global loan_amount,monthly_payment
	loan_amount = input("Loan Amount:")
	monthly_payment = input("Monthly Payment:")

def cal_payments():
	