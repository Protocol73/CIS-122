# Alphbetic Page Number Finder By Protocol73
# Writen for CIS-122 
# Not for use Outside Lab or Classroom

import os
import sys
import time

try: #for py v2 vs v3 input
    input = raw_input
except NameError:
    pass

search_word = "" #Clear the value
current_page = 0
pos_check = 0

#Static Functions

def clear_screen(): #clear the Screen
    os.system('cls' if os.name=='nt' else 'clear')
    #works on PC & Mac
def Welcome_Screen():#Startup Screen
	clear_screen()
	print("Welcome to Protocol73's Page Finder.")
	print("For Finding a word in an Dictionary by Page Number.")
def restart_program():#Restarts the program
	#Warning,Restarts without cleanup
	os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

#User Input Fuctions

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
		clear_screen()
		return -1
def pages_in_dict():#Number of Pages in Dictionary
	total_pages = input("Enter the Total Number of Pages in the Dictionary:")
	if not total_pages.isdigit():
		print("\nError:Not a usable number.")
		time.sleep(2)
		clear_screen()
		pages_in_dict()
	else:
		print("\nYou Entered:", total_pages, "Is this Correct?",)
		if Check_Prompt()is True:
			return total_pages
		else:
			clear_screen()
			restart_program()
def word_to_find():#Ask the User what word to look for
	global search_word,search_word_as_num
	search_word = input("Word to Find:")
	search_word_as_num = word_to_numbers(search_word)

	return search_word

#Data Functions

def dict_start_page(): #start looking here
	global current_page,search_word #keep track of where we are
	word = search_word
	total_pages_in_dict = pages_in_dict()
	num_of_first_letter = word_to_numbers(word)[0] 
	pages_per_letter = int(total_pages_in_dict) / 26
	start_page = pages_per_letter * num_of_first_letter
	current_page = int(start_page)
	clear_screen()
	print("Turn to page " + str(current_page))
	return int(start_page) #Start looking here

def word_to_numbers(word):#Convert letters to numbers
	#input_word = input('Word to find:') #Need User Input Word
	#input_word = input_word.lower()
	output = []
	for character in word:
		number = ord(character) - 96
		output.append(number)
	return output
def page_head_word():#Return first four letters of word as numbers
	global headword_as_number
	headword = input("Enter The headword from page:",)
	headword = str(headword)
	headword_as_number = word_to_numbers(headword)
	return headword_as_number

def real_search():
	global current_page,pos_check
	while True:
		if search_word_as_num == headword_as_number:
			print("You Found it!")
			time.sleep(2)
			clear_screen()
			break
		else:
			if search_word_as_num[pos_check] == headword_as_number[pos_check]:
				pos_check = pos_check + 1
				continue
			elif search_word_as_num > headword_as_number:
				turn_direction = "forward"
			else:
				turn_direction = "back"

			if pos_check == 0:
				if turn_direction == "back":
					current_page = current_page - 12
				else:
					current_page = current_page + 12
				print("Turn " + turn_direction + " 12 pages to " + str(current_page) + ":")
				page_head_word()
				continue
			elif pos_check == 1:
				if turn_direction == "back":
					current_page = current_page - 6
				else:
					current_page = current_page + 6
				print("Turn " + turn_direction + " 6 pages to " + str(current_page) + ":")
				page_head_word()
				continue
			elif pos_check == 2:
					print("Turn " + turn_direction +  " 3 or less pages.")
					page_head_word()
					continue
			elif pos_check == 2:
				print("Check this page & the next  " + turn_direction)
				current_page = current_page + 1
				page_head_word()
				continue
			else:
				print("\nYour Word Should be on this Page.")
				print("Is " + search_word +  " Here?")
				if Check_Prompt() is True:
					clear_screen()
					print("Complete")
					return 0
					sys.exit()
				else:
					print("Error: This program is not Built to check more then the first four letters.")
					print("Check one page back & one forward")
					time.sleep(2)
					print("If it's not there, \nYour word is not in the Dictionary or your dictionary is to big")

def main():
	Welcome_Screen()
	word_to_find()
	dict_start_page()
	page_head_word()
	real_search()

main()

