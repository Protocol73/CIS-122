#dictionary-lookup.py

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

#Program Fuctions

def initialize():
	global found,word,max_pages
	found = False
	search_word = ""
	max_pages = 0

def word_to_numbers(word):#Convert letters to numbers
	output = []
	for character in word:
		number = ord(character) - 96
		output.append(number)
	return output

def math_startpage():#get a place to start
	global startpage,pages_per_letter,current_page
	pages_per_letter = int(total_pages)/26
	first_letter_in_search_word = word_to_numbers(search_word)[0]
	startpage = first_letter_in_search_word * pages_per_letter
	current_page = startpage

def Welcome_Screen():#Startup Screen
	clear_term()
	print("Welcome to Protocol73's Page Finder.")
	print("For Finding a word in an Dictionary via Page Number.")

def pages_in_dict():#Number of Pages in Dictionary
	global total_pages
	get_total_pages = input("Enter the Total Number of Pages in the Dictionary:")
	if not get_total_pages.isdigit():
		print("\nError:Not a usable number.")
		time.sleep(2)
		clear_term()
		return -1
	else:
		print("\nYou Entered:", get_total_pages, "Is this Correct?",)
		if check_prompt() is True:
			total_pages = get_total_pages
			return int(total_pages)
		else:
			clear_term()
			return -1

def word_to_find():#Ask the User what word to look for
	global search_word,search_word_as_num
	search_word = input("Word to Find:")
	print("Is the search word:", search_word, "?" )
	if check_prompt() is True:
		search_word_as_num = word_to_numbers(search_word)
		return search_word
	else:
		return -1
	
def page_head_word():#Return first four letters of word as numbers
	global headword_as_number
	headword = input("Enter The headword from page " + str(int(current_page)) + ":")
	headword = str(headword)
	headword_as_number = word_to_numbers(headword)
	return headword_as_number


def real_search():#search for the word
	global current_page,pos_check
	pos_check = 0
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
			elif search_word_as_num[pos_check] > headword_as_number[pos_check]:
				turn_direction = "forward"
			else:
				turn_direction = "back"

			if pos_check == 0:
				distance_0 = abs(search_word_as_num[0] - headword_as_number[0])
				if turn_direction == "back":
					if distance_0 is 1:
						current_page = current_page - pages_per_letter / 4
					elif distance_0 is 2:
						current_page = current_page - pages_per_letter / 2
					else:
						current_page = current_page - pages_per_letter 
				else:
					if distance_0 is 1:
						current_page = current_page + pages_per_letter / 2
					elif distance_0 is 2:
						current_page = current_page + pages_per_letter 
					else:
						current_page = current_page - pages_per_letter * 1.5
				
				print("Turn " + turn_direction + " to page " + str(int(current_page)) + ":")
				page_head_word()
				continue
			elif pos_check == 1:
				distance_1 = abs(search_word_as_num[1] - headword_as_number[1])
				if turn_direction == "back":
					if distance_1 < 10:
						current_page = current_page - pages_per_letter / 25
					elif distance_1 > 10:
						current_page = current_page - pages_per_letter / 20
					else:
						current_page = current_page - pages_per_letter / 10
				else:
					if distance_1 < 10:
						current_page = current_page + pages_per_letter / 15
					elif distance_1 > 10:
						current_page = current_page + pages_per_letter / 10
					else:
						current_page = current_page - pages_per_letter / 5
				
				print("Turn " + turn_direction + " to page " + str(int(current_page)) + ":")
				page_head_word()
				continue

			elif pos_check == 2:#
				if search_word_as_num[2] < headword_as_number[2]:
					current_page = current_page - 1
					print("Turn " + turn_direction + " to page " + str(int(current_page)) + ":")
					page_head_word()
					continue
				headword_last = input("Enter the last word on page " + str(int(current_page)) + ":")
				distance_2 = abs(search_word_as_num[2] - headword_as_number[2])
				check_range_page = range(headword_as_number[2], word_to_numbers(headword_last)[2])
				if search_word_as_num[2] in check_range_page:
					print("\nYour Word Should be on this Page.")
					print("Is the word " + search_word +  " Here?")
					if check_prompt() is True:
						clear_term()
						print("Complete")
						return 0
						sys.exit()
					else:
						if turn_direction == "back":
							if distance_2 < 15:
								current_page = current_page - 1
							else:
								current_page = current_page - 2
						else:
							if distance_2 < 15:
								current_page = current_page + 1
							else:
								current_page = current_page + 2
				else:
					pos_check = 3

		
			elif pos_check == 3:
				print("\nYour Word Should be on this Page.")
				print("Is  the word " + search_word +  " Here?")
				if check_prompt() is True:
					clear_term()	
					print("Complete")
					return 0
					sys.exit()
			else:
				print("Error: This program is not Built to check more then the first four letters.")
				print("Check one page back & one forward")
				time.sleep(2)
				print("If it's not there, \nYour word is not in the Dictionary or your dictionary is to large")


def main():
	clear_term()
	initialize()
	Welcome_Screen()
	while word_to_find() is -1:
		continue
	else:
		pass
	while pages_in_dict() <2:
		print("You need a Dictionary with more then 1 page.")
		continue
	else:
		pass
	math_startpage()
	page_head_word()
	real_search()

main()
