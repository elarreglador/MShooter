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
		
# funcion lee
def lee(archivo):
	with open(archivo, 'r') as file:
		contenido = file.read().replace('\n', '')
		return contenido

#MAIN
cls()
asteriscos ("Mecanography Shooter\n By El Arreglador")
pausa()
print(lee("./lvl/01.txt"))
