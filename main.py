#!/usr/bin/python3
# -*- coding: utf-8 -*-

# CIFRADO CÉSAR

from coded import coded
from decoded import decoded
import sys

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