import random
import win32api
import time
from ctypes import windll
import pyautogui
from datetime import datetime
from WindowsVirtualKeyCodes import WindowsVirtualKeyCodes

# Establishing the keyboard module
output = WindowsVirtualKeyCodes()

# Variable to store
facts_said = []
second_pos = 0

#Timeout period to deactivate
time_limit = 30

# Press Keyboard key
def press_key(key):
	output.type(key)

# Get that random fact for me without repeating
def random_fact():
	global facts_said

	# Only open files if we need to
	try: facts
	except NameError: 
		with open(r"random_facts.txt") as file_in:
			facts = file_in.readlines()
			file_in.close()
		

	# Loop until a new, ungathered, fact is found
	new_fact_found = False
	while new_fact_found == False:
		fact_num = random.randint(0, len(facts)-1)
		if fact_num not in facts_said:
			# Add fact to list of already said things and return the fact
			facts_said.append(fact_num)
			return facts[fact_num]
		# Just print that we are working
		else:
			print('Repeat - Finding next fact')
			
# The way to type into the csgo message
def type_in_csgo(message):
	#time.sleep(.1
	output.type(message)

# Wait for user to type Y (This way we arent "hacking")
def wait_for_y():
	print('press y to continue')
	state_fact = False
	not_pressed = True
	while not_pressed:
		if (win32api.GetAsyncKeyState(output.Y) < 0):
			time.sleep(.1)
			not_pressed = False
	time.sleep(.2)


def do_the_typing(first):
	first = first
	# We want to second_pos to save
	global second_pos
	# Only open files if we need to
	try: things_to_say
	except NameError:
		with open("things_to_say.txt") as content:
			things_read = content.readlines()
	first_pos = 0
	loop_var = first
	time.sleep(.5)
	while loop_var:
		type_in_csgo(things_read[first_pos])
		first_pos += 1
		if '~0~' in things_read[first_pos]:
			second_pos = first_pos + 1
			loop_var = False
			wait_for_y()
		else:
			wait_for_y()
	end = False
	second_counter = second_pos
	while not first and not end:
		type_in_csgo(things_read[second_counter])
		second_counter += 1
		if second_counter >= len(things_read):
			end = True
			second_counter = second_pos
			wait_for_y()
		else:
			wait_for_y()
	type_in_csgo(random_fact())

def the_program():
	while True:
		program_switch = False
		first = True
		if (win32api.GetAsyncKeyState(output.F1) < 0):
			time.sleep(.6)
			program_switch = True
			start_time = datetime.now()
			first_thing = True

	
		while program_switch == True:
			timer = datetime.now()
			if (win32api.GetAsyncKeyState(output.Y) < 0):
				start_time = datetime.now()
				do_the_typing(first_thing)
				first_thing = False
				time.sleep(.5)
			elif (win32api.GetAsyncKeyState(output.F1) < 0):
				time.sleep(1)
				program_switch = False

			# Time out the program_switch so there are no accidental hits when going to actually type
			if (timer-start_time).seconds >= time_limit:
				program_switch = False

the_program()
