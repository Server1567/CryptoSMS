#!/usr/bin/python3
# -*- coding: utf-8 -*-

# MÉTODO DE CIFRADO CÉSAR

def coded():
	file = input("Name file to code => ")
	txt = open(file, "r")
	text = txt.read()
	key = input("Type the key(8 chr min) => ")
	ciphered_text = get_cipher(key, text)
	txt.close()
	f = open("cifrado.txt", "w")

	try:
		f.write(ciphered_text)
	except UnicodeEncodeError as e:
		print("We find a character that can't be encrypted :/")
		print("Characters not allowed: ° - ´ - ¿ ")
		
	f.close()

def get_cipher(key, plain_text):
	cif = ""
	for index, val in enumerate(plain_text):
		c = ord(val) ^ ord(key[7])
		cif += str(chr(c))
	return cif