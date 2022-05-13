#!/usr/bin/python3

import os
import random
import time


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

# funcion pinta: pinta el caracter X en la linea Y y la columna Z
def pinta(X,Y,Z):
	while Y > 0:
		print ()
		Y = Y - 1
	while Z > 0:
		print ("", end=" ")
		Z = Z - 1
	print (X)

#MAIN
cls()
asteriscos ("Mecanography Shooter\n By El Arreglador")
pausa()
nivel=10
cls()
while 1==1:
	asteriscos ("Bienvenido al nivel "+str(nivel)+".")
	print ("\n"+lee("./lvl/"+str(nivel)+".info")+"\n")
	pausa()
	cls()
	matriz = var2matrix(lee("./lvl/"+str(nivel)+".txt"))
	horainicio = time.time()
	fallos = 0
	exitos = 0
	msg = "Pulsa la letra que se muestra arriba lo mas rapido que puedas y pulsa Intro con el meñique."
	print ("Exitos: " + str(exitos) + "   Fallos: " + str(fallos))
	intentos=int(matriz[0])
	while intentos >= 1: #Num de ciclos indicado en archivo del nivel
		lenMatriz=len(matriz)-1
		objetivo = (matriz[random.randint(1,lenMatriz)]) #caracter que debemos pulsar
		Y = random.randint(0,10)
		Z = random.randint(0,80)
		pinta (objetivo, Y, Z) #pinta el objetivo en una posicion aleatoria
		pinta (msg,15-Y,0)
		entrada = input()
		if entrada == objetivo:
			exitos = exitos + 1
		else:
			fallos = fallos + 1
		intentos = intentos - 1
		cls()
		print ("Exitos: " + str(exitos) + "   Fallos: " + str(fallos))
	horafin = time.time()

	# Estadistica
	diferencia = horafin - horainicio
	intDiferencia = int(diferencia)
	pulsaciones = exitos + fallos
	precision = (exitos * 100) / pulsaciones
	cls()
	asteriscos ("Exitos: " + str(exitos) + "   Fallos: " + str(fallos) + "\n Tiempo : " + str(intDiferencia) + "\n Precision: " + str(precision) + "%")
	nivel=nivel+1



