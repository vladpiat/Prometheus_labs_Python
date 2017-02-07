def encode_morze(text):
	morse_code = {
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
	}



	clear_text = " "               #upper text, contains only symbols of alphabet
	morse_text = None				#
	morse_encoded_text = None
	morse_diag = morse_code.copy()
	morse_diag.clear()
	chars_allowed=morse_code.keys() + list(' ') #array of allowed keys
	upper_text=text.upper() #getting string UPPER
	for curent_char in upper_text:				#geting  clear text
		if (curent_char in chars_allowed):
			if not(clear_text):
				clear_text=curent_char
			else:
				clear_text=clear_text+curent_char
	clear_text = clear_text.split(" ")


	for current_char in morse_code.keys(): 					#geting dictionary of symbols of alphabet and morse diagram (like ^_^^^_^ mean .-.)
		morse_symbol = None
		for current_symbol in morse_code.get(current_char):
			if morse_symbol:
				if current_symbol == "-":
					morse_symbol = morse_symbol + "_^^^"
				else:
					morse_symbol = morse_symbol + "_^"
			else:
				if current_symbol == "-":
					morse_symbol = "^^^"
				else:
					morse_symbol = "^"

		morse_diag[current_char] = morse_symbol

	for current_word in clear_text:
		morse_encoded_word = None
		for current_char in current_word:
			if morse_encoded_word:
				morse_encoded_word = morse_encoded_word + "___" + morse_diag.get(current_char,None)
			else:
				morse_encoded_word = morse_diag.get(current_char,None)
		if morse_encoded_word:
			if morse_encoded_text:
				morse_encoded_text = morse_encoded_text + "_"*7 + morse_encoded_word
			else:
				morse_encoded_text =  morse_encoded_word
	if not(morse_encoded_text):
		morse_encoded_text = " "

	return morse_encoded_text


print encode_morze('shmiga daun')
