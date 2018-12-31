#!/usr/bin/python3
# -*- coding: utf-8 -*-

# CIFRADO CÉSAR

import sys, time

# MÉTODO DE CIFRADO CÉSAR

def coded():
	file = input("Nombre del archivo a cifrar => ")

	try:
		txt = open(file, "r")
		text = txt.read()
	except Exception as e:
		print("Asegurese de que el archivo se encuentre en la misma carpeta :/")
		time.sleep(5)
		sys.exit()

	key = input("Escriba la clave(8 chr min) => ")
	ciphered_text = get_cipher(key, text)
	txt.close()
	f = open("cifrado.txt", "w")

	try:
		f.write(ciphered_text)
	except UnicodeEncodeError as e:
		print("Encontramos un carácter que no puede ser encriptado :/")
		print("Carácteres no permitidos: ° - ´ - ¿ ")
		
	f.close()

def get_cipher(key, plain_text):
	cif = ""
	for index, val in enumerate(plain_text):
		c = ord(val) ^ ord(key[7])
		cif += str(chr(c))
	return cif

# MÉTODO DE DESIFRADO CÉSAR

def decoded():
	try:
		key = input("Escriba la clave => ")
		f = open("cifrado.txt", "r")
		ctext = f.read()
	except FileNotFoundError as e:
		print("Asegurese de escribir 'cifrado.txt'")
		time.sleep(5)
		sys.exit()

	plain_text = ""
	for index, val in enumerate(ctext):
		c = ord(val) ^ ord(key[7])
		plain_text += str(chr(c))

	mensaje = open("mensaje_desifrado.txt", "w")
	mensaje.write(plain_text)
	mensaje.close()

if __name__ == "__main__":
	print("")
	print("************************************")
	print("***** SISTEMA DE CIFRADO CÉSAR *****")
	print("************************************")
	print("     ~ SELECCIONE UNA OPCIÓN ~      ")
	print("")
	print("1. Cifrar")
	print("2. Desifrar")
	print("3. Salir")
	print("")

	option = input("=> ")
	if option == str(1):
		coded()

	elif option == str(2):
		decoded()

	elif option == str(3):
		sys.exit()

	else:
		print("La opción no se encuentra en el menú. SELECCIONE 1, 2 o 3")
		time.sleep(5)
		sys.exit()
