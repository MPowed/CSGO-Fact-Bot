#https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN

# Windows virtual key codes with the necassary code to use
import win32api
import win32con
import time


#Microsoft Virtual Key Codes
class WindowsVirtualKeyCodes:
	def __init__(self):
		self.keyToPress    = ''
		self.w32KeyUp      = win32con.KEYEVENTF_KEYUP
		self.keyboard_event = win32api.keybd_event
		self.mouse_event    = win32api.mouse_event
		self.cursorPOS     = win32api.SetCursorPos
		self.mouse_left_down = win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0
		self.mouse_left_up   = win32con.MOUSEEVENTF_LEFTUP,0,0,0,0
		self.mouse_right_down = win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0
		self.mouse_right_up   = win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0
		self.cursorPOS     = win32api.SetCursorPos

		self.left_mouse   = 0x01	# Left mouse button 										# VK_LBUTTON
		self.right_mouse  = 0x02    # Right mouse button 										# VK_RBUTTON
		self.cancel 	  = 0x03    # Control-break processing									# VK_CANCEL 
		self.middle_mouse = 0x04 	# Middle mouse button (three-button mouse)					# VK_MBUTTON
		self.x1_mouse 	  = 0x05 	# X1 mouse button 											# VK_XBUTTON1
		self.x2_mouse 	  = 0x06 	# X2 mouse button 											# VK_XBUTTON2
		self.back         = 0x08 	# BACKSPACE key 											# VK_BACK
		self.tab 	      = 0x09 	# TAB key 													# VK_TAB
		self.clear        = 0x0C 	# CLEAR key 												# VK_CLEAR
		self.enter_key 	  = 0x0D 	# ENTER key 												# VK_RETURN
		self.shift_key 	  = 0x10 	# SHIFT key 												# VK_SHIFT
		self.ctrl_key 	  = 0x11 	# CTRL key 													# VK_CONTROL
		self.alt     	  = 0x12 	# ALT key 													# VK_MENU
		self.pause_key 	  = 0x13 	# PAUSE key 												# VK_PAUSE
		self.caps_lock 	  = 0x14 	# CAPS LOCK key 											# VK_CAPITAL
		self.esc_key 	  = 0x1B 	# ESC key 													# VK_ESCAPE
		self.space_key    = 0x20 	# SPACEBAR   												# VK_SPACE 	
		self.page_up  	  = 0x21 	# PAGE UP key                  								# VK_PRIOR 	
		self.page_down	  = 0x22 	# PAGE DOWN key 											# VK_NEXT 		
		self.end_key 	  = 0x23 	# END key 													# VK_END 
		self.home_key 	  = 0x24 	# HOME key 													# VK_HOME 	
		self.left_arrow   = 0x25 	# LEFT ARROW key 											# VK_LEFT 	 	
		self.up_arrow 	  = 0x26 	# UP ARROW key 												# VK_UP
		self.right_arrow  = 0x27 	# RIGHT ARROW key 											# VK_UP
		self.down_arrow   = 0x28 	# DOWN ARROW key 											# VK_DOWN 	 	
		self.select_key   = 0x29 	# SELECT key 												# VK_SELECT	
		self.print_key 	  = 0x2A 	# PRINT key 												# VK_PRINT  	
		self.execute_key  = 0x2B 	# EXECUTE key 												# VK_EXECUTE	
		self.print_screen = 0x2C 	# PRINT SCREEN key 											# VK_SNAPSHOT 	
		self.insert_key   = 0x2D 	# INS key 													# VK_INSERT	
		self.delete_key   = 0x2E 	# DEL key 													# VK_DELETE	
		self.help_key	  = 0x2F 	# HELP key 													# VK_HELP 


		self.zero_key    = 0x30 	# 0 key
		self.one_key	 = 0x31 	# 1 key
		self.two_key     = 0x32 	# 2 key
		self.three_key   = 0x33 	# 3 key
		self.four_key	 = 0x34 	# 4 key
		self.five_key	 = 0x35 	# 5 key
		self.six_key 	 = 0x36 	# 6 key
		self.seven_key	 = 0x37 	# 7 key
		self.eight_key	 = 0x38 	# 8 key
		self.nine_key	 = 0x39 	# 9 key

		self.A =	0x41 	# A key
		self.B =	0x42 	# B key
		self.C =	0x43 	# C key
		self.D =	0x44 	# D key
		self.E =	0x45 	# E key
		self.F =	0x46 	# F key
		self.G =	0x47 	# G key
		self.H =	0x48 	# H key
		self.I =	0x49 	# I key
		self.J =	0x4A 	# J key
		self.K =	0x4B 	# K key
		self.L =	0x4C 	# L key
		self.M =	0x4D 	# M key
		self.N = 	0x4E 	# N key
		self.O =	0x4F 	# O key
		self.P =	0x50 	# P key
		self.Q =	0x51 	# Q key
		self.R =	0x52 	# R key
		self.S =	0x53 	# S key
		self.T =	0x54 	# T key
		self.U =	0x55 	# U key
		self.V =	0x56 	# V key
		self.W =	0x57 	# W key
		self.X =	0x58 	# X key
		self.Y =	0x59 	# Y key
		self.Z =	0x5A 	# Z key	
		self.left_windows_key   = 0x5B 	# Left Windows key (Natural keyboard) 					# VK_LWIN  	
		self.right_windows_key  = 0x5C 	# Right Windows key (Natural keyboard) 					# VK_RWIN
		self.app_key          	= 0x5D 	# Applications key (Natural keyboard) 					# VK_APPS 	
		self.comp_sleep_key     = 0x5F 	# Computer Sleep key 									# VK_SLEEP
		self.zero_numpad 	= 0x60 	# Numeric keypad 0 key 										# VK_NUMPAD0
		self.one_numpad     = 0x61 	# Numeric keypad 1 key 										# VK_NUMPAD1 	
		self.two_numpad		= 0x62 	# Numeric keypad 2 key 										# VK_NUMPAD2
		self.three_numpad 	= 0x63 	# Numeric keypad 3 key 										# VK_NUMPAD3
		self.four_numpad 	= 0x64 	# Numeric keypad 4 key 										# VK_NUMPAD4 	 	
		self.five__numpad	= 0x65 	# Numeric keypad 5 key 										# VK_NUMPAD5 	
		self.six_numpad		= 0x66 	# Numeric keypad 6 key 										# VK_NUMPAD6 	
		self.seven_numpad	= 0x67 	# Numeric keypad 7 key 										# VK_NUMPAD7 	
		self.eight_numpad	= 0x68 	# Numeric keypad 8 key 										# VK_NUMPAD8 	
		self.nine_numpad	= 0x69 	# Numeric keypad 9 key 										# VK_NUMPAD9 	
		self.multiply_key	= 0x6A 	# Multiply key 												# VK_MULTIPLY 	
		self.add_key		= 0x6B 	# Add key 													# VK_ADD
		self.seperator_key	= 0x6C 	# Separator key 											# VK_SEPARATOR 	 	
		self.subtract_key	= 0x6D 	# Subtract key 												# VK_SUBTRACT 	
		self.decimal_key	= 0x6E 	# Decimal key 												# VK_DECIMAL 	
		self.divide_key		= 0x6F 	# Divide key 												# VK_DIVIDE 	
		self.F1	= 0x70 		# F1 key 									# VK_F1	
		self.F2  = 0x71 	# F2 key 									# VK_F2 	
		self.F3  = 0x72 	# F3 key 									# VK_F3	
		self.F4  = 0x73 	# F4 key 									# VK_F4	
		self.F5  = 0x74 	# F5 key 									# VK_F5	
		self.F6  = 0x75 	# F6 key 									# VK_F6	
		self.F7  = 0x76 	# F7 key 									# VK_F7	
		self.F8  = 0x77 	# F8 key 									# VK_F8	
		self.F9  = 0x78 	# F9 key 									# VK_F9	
		self.F10 = 0x79 	# F10 key 									# VK_F10 	
		self.F11 = 0x7A 	# F11 key 									# VK_F11	
		self.F12 = 0x7B 	# F12 key 									# VK_F12
		self.F13 = 0x7C 	# F13 key 									# VK_F13 	
		self.F14 = 0x7D  	# F14 key 									# VK_F14 	
		self.F15 = 0x7E 	# F15 key                                   # VK_F15	
		self.F16 = 0x7F 	# F16 key 									# VK_F16	
		self.F17 = 0x80 	# F17 key 									# VK_F17 	 	 
		self.F18 = 0x81 	# F18 key 									# VK_F18 	
		self.F19 = 0x82 	# F19 key 									# VK_F19 	
		self.F20 = 0x83 	# F20 key 									# VK_F20 	
		self.F21 = 0x84 	# F21 key 									# VK_F21	
		self.F22 = 0x85 	# F22 key 									# VK_F22 	
		self.F23 = 0x86 	# F23 key 									# VK_F23 	
		self.F24 = 0x87 	# F24 key 									# VK_F24
 	
		self.num_lock    		 = 0x90 	# NUM LOCK key 					# VK_NUMLOCK
		self.scroll_lock 		 = 0x91 	# SCROLL LOCK key               # VK_SCROLL	
		self.left_shift_key      = 0xA0 	# Left SHIFT key 				# VK_LSHIFT 	
		self.right_shift_key     = 0xA1 	# Right SHIFT key 				# VK_RSHIFT 	
		self.left_ctrl_key       = 0xA2 	# Left CONTROL key 				# VK_LCONTROL 	 	
		self.right_ctrl_key      = 0xA3 	# Right CONTROL key 			# VK_RCONTROL	
		self.left_menu_key       = 0xA4 	# Left MENU key 				# VK_LMENU 	
		self.right_menu_key      = 0xA5 	# Right MENU key   				# VK_RMENU 	
		self.browser_back_key    = 0xA6 	# Browser Back key 				# VK_BROWSER_BACK 	
		self.browser_forward_key = 0xA7 	# Browser Forward key 			# VK_BROWSER_FORWARD  	
		self.browser_refresh_key = 0xA8 	# Browser Refresh key 			# VK_BROWSER_REFRESH 	
		self.browser_stop_key    = 0xA9 	# Browser Stop key 				# VK_BROWSER_STOP 	
		self.browser_search_key  = 0xAA 	# Browser Search key 			# VK_BROWSER_SEARCH 	
		self.browser_fav_key     = 0xAB 	# Browser Favorites key 		# VK_BROWSER_FAVORITES	
		self.browser_home_key    = 0xAC 	# Browser Start and Home key 	# VK_BROWSER_HOME  	
		self.vol_mute         = 0xAD 	# Volume Mute key 					# VK_VOLUME_MUTE 	
		self.vol_down         = 0xAE 	# Volume Down key					# VK_VOLUME_DOWN 	
		self.vol_up           = 0xAF 	# Volume Up key 					# VK_VOLUME_UP	
		self.media_next   	  = 0xB0 	# Next Track key 					# VK_MEDIA_NEXT_TRACK 	
		self.media_prev       = 0xB1 	# Previous Track key 				# VK_MEDIA_PREV_TRACK  	
		self.media_stop       = 0xB2 	# Stop Media key 					# VK_MEDIA_STOP	
		self.media_play_pause = 0xB3 	# Play/Pause Media key 				# VK_MEDIA_PLAY_PAUSE  	
		self.mail_key         = 0xB4 	# Start Mail key 					# VK_LAUNCH_MAIL
		self.launch_media_key = 0xB5 	# Select Media key 					# VK_LAUNCH_MEDIA_SELECT 	
		self.start_app_1      = 0xB6 	# Start Application 1 key           # VK_LAUNCH_APP1	
		self.start_app_2      = 0xB7 	# Start Application 2 key 			# VK_LAUNCH_APP2 


		# OEM Stuff

			
		self.plus_key   = 0xBB 	# For any country/region, the '+' key 								# VK_OEM_PLUS 
		self.comma_key  = 0xBC 	# For any country/region, the ',' key 								# VK_OEM_COMMA
		self.minus_key  = 0xBD 	# For any country/region, the '-' key 								# VK_OEM_MINUS 		
		self.period_key = 0xBE 	# For any country/region, the '.' key 								# VK_OEM_PERIOD	
		self.oem_1_key  = 0xBA 	# For the US keyboard, the ';:' key 								# VK_OEM_1 
							# Used for miscellaneous characters; it can vary by keyboard.  				
		self.oem_2_key  = 0xBF 	# For the US keyboard, the '/?' key 								# VK_OEM_2 	
							# Used for miscellaneous characters; it can vary by keyboard. 						
		self.oem_3_key  = 0xC0 	# For the US keyboard, the '`~' key 								# VK_OEM_3
							# Used for miscellaneous characters; it can vary by keyboard. 						
		self.oem_4_key  = 0xDB 	# For the US keyboard, the '[{' key 								# VK_OEM_4
							# Used for miscellaneous characters; it can vary by keyboard. 					
		self.oem_5_key  = 0xDC 	# For the US keyboard, the '\|' key   								# VK_OEM_5 	
							# Used for miscellaneous characters; it can vary by keyboard. 					
		self.oem_6_key  = 0xDD 	# For the US keyboard, the ']}' key 								# VK_OEM_6
							# Used for miscellaneous characters; it can vary by keyboard. 	
		self.oem_7_key  = 0xDE 	# For the US keyboard, the 'single-quote/double-quote' key 			# VK_OEM_7
							# Used for miscellaneous characters; it can vary by keyboard. 					
		self.oem_8_key  = 0xDF 	# Used for miscellaneous characters; it can vary by keyboard. 		# VK_OEM_8 	


		"""
		# No need for these, Included to show all virtual key codes

		VK_OEM_102 		0xE2 	Either the angle bracket key or the backslash key on the RT 102-key keyboard
						0xE1 	OEM specific
						0xE3-E4 	OEM specific
						0x92-96 	OEM specific
			
		VK_ATTN 		0xF6 	Attn key
		VK_CRSEL 		0xF7 	CrSel key
		VK_EXSEL 		0xF8 	ExSel key
		VK_EREOF 		0xF9 	Erase EOF key
		VK_PLAY 		0xFA 	Play key
		VK_ZOOM 		0xFB 	Zoom key
		VK_NONAME 		0xFC 	Reserved
		VK_PA1 	        0xFD 	PA1 key
		VK_OEM_CLEAR 	0xFE 	Clear key

		# Language input method editors.
		VK_PROCESSKEY 	0xE5 	# IME PROCESS key	
		VK_KANA 	    0x15 	# IME Kana mode
		VK_HANGUL 	    0x15 	# IME Hangul mode
		VK_IME_ON 	    0x16 	# IME On
		VK_JUNJA 	    0x17 	# IME Junja mode
		VK_FINAL 	    0x18 	# IME final mode
		VK_HANJA 	    0x19 	# IME Hanja mode
		VK_KANJI 	    0x19 	# IME Kanji mode
		VK_IME_OFF      0x1A 	# IME Off
		VK_CONVERT      0x1C 	# IME convert
		VK_NONCONVERT   0x1D 	# IME nonconvert
		VK_ACCEPT 		0x1E 	# IME accept
		VK_MODECHANGE 	0x1F 	# IME mode change request


		# Undefined / Unassigned / Reserved
		 -  0x07 	    Undefined
		 - 	0x0A-0B     Reserved
		 - 	0x0E-0F 	Undefined
		 - 	0x3A-40 	Undefined
		 - 	0x5E 	    Reserved
		 - 	0x88-8F 	Unassigned
		 - 	0x97-9F 	Unassigned
		 - 	0xB8-B9 	Reserved
		 - 	0xC1-D7 	Reserved
		 - 	0xD8-DA 	Unassigned
		 - 	0xE0 	    Reserved
		"""









##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
	
	# Method that updates the necassary things to press a key
	def update_key_to_press(self, key):
		if isinstance(key, str):
			self.key_to_press = self.translate_key_code(key)
		else:
			self.key_to_press = key
		self.press = self.key_to_press, 0, 0, 0
		self.depress = self.key_to_press, 0, self.w32KeyUp, 0

	def translate_key_code(self, key):
		# A Work in progress. hypothetically this needs to have every character translation available
		keyCode = {
		'shift' : self.shift_key,
			'0' : self.zero_key,
			'1' : self.one_key,
			'2' : self.two_key,
			'3' : self.three_key,
			'4' : self.four_key,
			'5' : self.five_key,
			'6' : self.six_key,
			'7' : self.seven_key,
			'8' : self.eight_key,
			'9' : self.nine_key,
			'a' : self.A,
			'b' : self.B,
			'c' : self.C,
			'd' : self.D,
			'e' : self.E,
			'f' : self.F,
			'g' : self.G,
			'h' : self.H,
			'i' : self.I,
			'j' : self.J,
			'k' : self.K,
			'l' : self.L,
			'm' : self.M,
			'n' : self.N,
			'o' : self.O,
			'p' : self.P,
			'q' : self.Q,
			'r' : self.R,
			's' : self.S,
			't' : self.T,
			'u' : self.U,
			'v' : self.V,
			'w' : self.W,
			'x' : self.X,
			'y' : self.Y,
			'z' : self.Z,
			' '     : self.space_key,
			'up'    : self.up_arrow,
			'down'  : self.down_arrow,
			'left'  : self.left_arrow,
			'right' : self.right_arrow,
			'"'     : self.oem_7_key,
			'\''    : self.oem_7_key,
			'.'     : self.period_key,
			'>'     : self.period_key,
			','     : self.comma_key,
			'<'		: self.comma_key,
			'/'		: self.oem_2_key,
			'?'		: self.oem_2_key,
			'\\'	: self.oem_5_key,
			'|'		: self.oem_5_key,
			':'     : self.oem_1_key,
			'\n'    : self.enter_key,
			'['     : self.oem_4_key,
			']'     : self.oem_6_key,
			'('     : self.nine_key,
			')'     : self.zero_key,
			'-'		: self.minus_key,
			'_'		: self.minus_key,
			'='		: self.plus_key,
			'+'		: self.plus_key,
			'~'		: self.oem_3_key
			}
		return keyCode.get(key.lower())



	# Push button accordingly(letter = Virtual Key Code)
	def push_button(self, button):
		self.update_key_to_press(button)
		self.keyboard_event(*self.press)
		time.sleep(.01)
		self.keyboard_event(*self.depress)

	# Type more then one letter
	def type(self, what):
		shift = False
		unique_characters = ['"', ':', '(', ')', '<', '>', '?', '{', '}', '~']
		for ch in what:
			if ch.isupper() or ch in unique_characters:
				shift = True
				self.hold_button('shift')
			self.push_button(ch)
			if shift == True:
				shift = False
				self.release_button('shift')

	# Mostly used for specific keys (i.e. shift, ctrl)
	def hold_button(self, button):
		self.update_key_to_press(button)
		self.keyboard_event(*self.press)

	def release_button(self, button):
		self.update_key_to_press(button)
		self.keyboard_event(*self.depress)


##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
	



	# Set the location of where you want the mouse
	def set_coords(self, x, y):
		self.mouseMoveArguements = win32con.MOUSEEVENTF_MOVE, x, y, 0, 0

	# Move the mouse to a specific location
	def move_mouse(self, x, y):
		self.set_coords(x, y)
		self.mouse_event(*self.mouseMoveArguements)

	# Left Click
	def left_click(self):
	    # Move the mouse if needed with move_mouse()
	    self.mouse_event(*self.mouse_left_down)
	    self.mouse_event(*self.mouse_left_up)

	def right_click(self):
		self.mouse_event(*self.mouse_right_down)
		self.mouse_event(*self.mouse_right_up)
