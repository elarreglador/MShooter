#!/usr/bin/python3

import os
import random

# función asteriscos: Encuadra un texto
def asteriscos(texto):
	print("**************************************************")
	print()
	print(" "+texto)
	print()
	print("**************************************************")	
	
# funcion pause: espera que pulses Intro
def pausa():
	input("\nPulsa Enter para continuar...")	
	
# funcion cls: borra la pantalla
def cls():
	if os.name == "posix":
		os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		os.system ("cls")
		
# funcion lee: devuelve el contenido de un archivo
def lee(archivo):
	with open(archivo, 'r') as file:
		contenido = file.read().replace('\n', '')
		return contenido
		
# funcion var2matrix: convierte una variable separada con ; a matriz
def var2matrix(var):
	varSplit = var.split(';')
	return varSplit

#MAIN
cls()
asteriscos ("Mecanography Shooter\n By El Arreglador")
pausa()
cls()

matriz = var2matrix(lee("./lvl/01.txt"))
numero=10
while numero >= 1:
	lenMatriz=len(matriz)-1
	objetivo = (matriz[random.randint(0,lenMatriz)])
	print (objetivo)
	numero = numero - 1
	



#print (matriz)
#print("Matriz tiene: " + str(len(matriz)) + " elementos.")







