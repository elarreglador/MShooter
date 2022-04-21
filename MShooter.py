#!/usr/bin/python3

import os

# función asteriscos
def asteriscos(texto):
	print("**************************************************")
	print()
	print(" "+texto)
	print()
	print("**************************************************")	
	
# funcion pause
def pausa():
	input("\nPulsa Enter para continuar...")	
	
# funcion cls
def cls():
	if os.name == "posix":
		os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		os.system ("cls")

#MAIN
cls()
asteriscos ("Mecanography Shooter\n By El Arreglador")
pausa()
