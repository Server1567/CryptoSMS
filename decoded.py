#!/usr/bin/python3
# -*- coding: utf-8 -*-

# MÉTODO DE DESIFRADO CÉSAR

def decoded():
	key = input("Type the key => ")
	f = open("cifrado.txt", "r")
	ctext = f.read()
	plain_text = ""
	for index, val in enumerate(ctext):
		c = ord(val) ^ ord(key[7])
		plain_text += str(chr(c))

	mensaje = open("mensaje_desifrado.txt", "w")
	mensaje.write(plain_text)
	mensaje.close()
